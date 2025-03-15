from notifypy import Notify

notifier = Notify()
notifier.application_name = "Battery Care Utility"
notifier.icon = "icon.png"
notifier.audio = "sound.wav"
notifier.message = ""

def seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return hours, minutes  

def notify(percentage, level, isUnlimited, time_left):
    hours, minutes = seconds_to_hms(time_left)
    notifier.message = ""

    match level:
        case "high":
            notifier.title = f"Unplug Charger • {percentage}%"
            if not isUnlimited:
                notifier.message = f"{hours} hours {minutes} minutes available. "
            notifier.message += f"Unplug the charger to avoid overcharging."

        case "low":
            notifier.title = f"Plug Charger • {percentage}%"
            if not isUnlimited:
                notifier.message = f"{hours} hours {minutes} minutes left. "
            notifier.message += f"Plug the charger to keep your device active."

        case _:
            notifier.title = f"Battery Percentage • {percentage}%"
            notifier.message = f"No action required. "
            if not isUnlimited:
                notifier.message += f"You have {hours} hours {minutes} minutes left."
    
    notifier.send()