import os
import platform
import shutil
from datetime import datetime

try:
    import psutil
except ImportError:
    print("Install the required library with: pip install psutil")
    raise


def bar(percent, width=25):
    filled = int(width * percent / 100)
    return "█" * filled + "░" * (width - filled)


def get_temperature():
    """Try to read CPU temperature on Linux."""
    try:
        temps = psutil.sensors_temperatures()
        for entries in temps.values():
            for entry in entries:
                if entry.current:
                    return f"{entry.current:.1f}°C"
    except (AttributeError, OSError):
        pass
    return "N/A"


def main():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = shutil.disk_usage(os.path.abspath(os.sep))
    disk_percent = disk.used / disk.total * 100

    net = psutil.net_io_counters()
    temp = get_temperature()

    print("\n" + "╔" + "═" * 46 + "╗")
    print("║" + " " * 13 + "HOMELAB DASHBOARD" + " " * 16 + "║")
    print("╠" + "═" * 46 + "╣")
    print(f"║ OS:      {platform.system()} {platform.release():<29}║")
    print(f"║ Host:    {platform.node():<35}║")
    print(f"║ Time:    {datetime.now().strftime('%Y-%m-%d %H:%M:%S'):<29}║")
    print("╠" + "═" * 46 + "╣")
    print(f"║ CPU      {bar(cpu)} {cpu:5.1f}%        ║")
    print(f"║ RAM      {bar(ram)} {ram:5.1f}%        ║")
    print(f"║ DISK     {bar(disk_percent)} {disk_percent:5.1f}%        ║")
    print(f"║ TEMP     {temp:<34}║")
    print("╠" + "═" * 46 + "╣")
    print("║ NETWORK                                  ║")
    print(f"║ ↓ Received: {net.bytes_recv / 1024**2:,.1f} MB{' ' * 19}║")
    print(f"║ ↑ Sent:     {net.bytes_sent / 1024**2:,.1f} MB{' ' * 19}║")
    print("╚" + "═" * 46 + "╝\n")


if __name__ == "__main__":
    main()
