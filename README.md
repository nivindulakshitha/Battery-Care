## 📌 Battery Care Utility

**Battery Care Utility** is a Python-based application that monitors your battery level and provides notifications when you need to **unplug** or **plug in** your charger. This helps prevent overcharging and ensures your device remains powered efficiently.

---

## 📜 Table of Contents
- [📌 Battery Care Utility](#-battery-care-utility)
- [📜 Table of Contents](#-table-of-contents)
- [🚀 Features](#-features)
- [🛠️ Installation](#️-installation)
- [📄 Usage](#-usage)
- [⚙️ Configuration (`configs.json`)](#️-configuration-configsjson)
- [🔔 Notifications](#-notifications)
- [💡 Troubleshooting](#-troubleshooting)
- [📜 License](#-license)

---

## 🚀 Features
✅ **Battery Monitoring**: Checks the battery percentage and charging status periodically.  
✅ **Smart Notifications**: Alerts when to unplug or plug in the charger.  
✅ **Customizable Settings**: Define your own battery thresholds in `configs.json`.  
✅ **Cross-Platform Support**: Works on **Windows** and **Linux** (Mac support may vary).  

---

## 🛠️ Installation

### 1️⃣ Install Dependencies
Ensure you have **Python 3.6+** installed on your system. Then, install the required Python packages:

```sh
pip install psutil notifypy
```

### 2️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/BatteryCareUtility.git
cd BatteryCareUtility
```

---

## 📄 Usage

Run the script using:

```sh
python app.py
```

The script will continuously monitor your battery status and send notifications when necessary.

---

## ⚙️ Configuration (`configs.json`)

You can customize the battery thresholds and enable/disable notifications by modifying the `configs.json` file.

Example:

```json
{
    "enabled": true,
    "max": 90,
    "min": 20
}
```

| Key       | Description                                        | Default |
|-----------|----------------------------------------------------|---------|
| `enabled` | Enables (`true`) or disables (`false`) monitoring | `true`  |
| `max`     | Percentage to notify to unplug charger            | `90`    |
| `min`     | Percentage to notify to plug in charger           | `20`    |

---

## 🔔 Notifications

The utility provides notifications in the following scenarios:

| Battery Level | Charging Status | Notification |
|--------------|-----------------|--------------|
| ≥ `max`%    | Plugged in       | "Unplug Charger" |
| ≤ `min`%    | Not plugged in   | "Plug Charger" |
| ≤ 10%       | Not plugged in   | "Critical Battery" |

---

## 💡 Troubleshooting

### 1️⃣ No Notifications Appearing
- **Windows**: Ensure `notifypy` works by running:
  ```sh
  python -c "from notifypy import Notify; Notify().send()"
  ```
  If no notification appears, try running `app.py` as **Administrator**.
  
- **Linux**: Install `libnotify`:
  ```sh
  sudo apt install libnotify-bin
  ```

### 2️⃣ `psutil.sensors_battery()` Returns `None`
- If running on a **desktop PC**, the function may return `None` because there is no battery.
- If on a **laptop**, ensure your battery drivers are correctly installed.

### 3️⃣ Sound Not Playing
- Ensure `sound.wav` exists and is supported.
- Try changing the sound file or using a different format.

---

## 📜 License
This project is licensed under the **Creative Common License**.