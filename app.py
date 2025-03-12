from Notifier import notify
import psutil
import time
import json

with open("configs.json", "r") as file:
    config = json.load(file)

notifications = {
    'max': False,
    'min': False,
}

while True and config['enabled']:
    BATTERY = psutil.sensors_battery()

    if BATTERY is None:
        break

    percentage = BATTERY.percent
    plugged = BATTERY.power_plugged
    time_left = BATTERY.secsleft
    isUnlimitedTime = time_left == psutil.POWER_TIME_UNLIMITED

    if plugged:
        notifications['max'] = False
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

    time.sleep(60)