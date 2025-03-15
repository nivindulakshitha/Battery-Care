from notifier import notify
import psutil
import time
import json

try: 
    with open("configs.json", "r") as file:
        config = json.load(file)
except Exception as e:
    print("Error reading configs.json", e)
    config = {
        "enabled": True,
        "min": 20,
        "max": 80
    }

notifications = {
    'max': False,
    'min': False,
}

waiting = 180

def decide_waiting(percentage, plugged):
    global waiting, config

    radius = 10

    if percentage <= config['min'] + radius and not plugged:
        waiting = 60

    elif percentage >= config['max'] - radius and plugged:
        waiting = 60

    else:
        waiting = 180
        

while True and config['enabled']:
    BATTERY = psutil.sensors_battery()

    if BATTERY is None:
        break

    percentage = BATTERY.percent
    plugged = BATTERY.power_plugged
    time_left = BATTERY.secsleft
    isUnlimitedTime = time_left == psutil.POWER_TIME_UNLIMITED

    decide_waiting(percentage, plugged)

    if plugged:
        notifications['max'] = notifications['max'] and True
        notifications['min'] = False

    # percentage is greater than or equal to 95 and plugged and notified
    if percentage >= 95 and notifications['max'] and plugged:
        notify(percentage, "high", isUnlimitedTime, time_left)

    # percentage is greater than or equal to max and not plugged
    elif percentage >= config['max'] and not notifications['max'] and plugged:
        notify(percentage, "high", isUnlimitedTime, time_left)
        notifications['max'] = True

    # percentage is less than or equal to min and not plugged
    elif percentage <= config['min'] and not notifications['min'] and not plugged:
        notify(percentage, "low", isUnlimitedTime, time_left)
        notifications['min'] = True

    # percentage is less than or equal to 10 and not plugged and notified
    elif percentage <= 10 and notifications['min'] and not plugged:
        notify(percentage, "low", isUnlimitedTime, time_left)

    time.sleep(waiting)