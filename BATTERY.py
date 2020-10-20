import psutil
from plyer import notification
import time

battery = psutil.sensors_battery()

while True:
    percent = battery.percent

    notification.notify(
        title="BATTERY PERCENTAGE",
        message=str(int(percent)) + "%BATTERY REMAINING",
        timeout=1000
    )
    
    time.sleep(60*3)
    
