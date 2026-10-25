import os
import platform
import shutil
import sys
from datetime import datetime

import psutil


def glyphs():
    try:
        "╔═╗║╠╣╚╝█░°".encode(sys.stdout.encoding or "utf-8")
        return "╔", "═", "╗", "║", "╠", "╣", "╚", "╝", "█", "░", "°C"
    except (UnicodeEncodeError, LookupError):
        return "+", "-", "+", "|", "+", "+", "+", "+", "#", ".", "C"


def temperature(unit):
    try:
        for entries in psutil.sensors_temperatures().values():
            for entry in entries:
                if entry.current is not None:
                    return f"{entry.current:.1f}{unit}" if unit == "°C" else f"{entry.current:.1f} C"
    except (AttributeError, OSError):
        pass
    return "N/A"


def main():
    tl, h, tr, v, ml, mr, bl, br, full, empty, unit = glyphs()
    width = 56

    def border(left, right):
        print(left + h * width + right)

    def row(value):
        print(v + " " + value[: width - 2].ljust(width - 2) + " " + v)

    def bar(label, value):
        value = max(0, min(100, value))
        filled = int(24 * value / 100)
        row(f"{label:<5} {full * filled}{empty * (24 - filled)} {value:5.1f}%")

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = shutil.disk_usage(os.path.abspath(os.sep))
    net = psutil.net_io_counters()

    border(tl, tr)
    row("HOMELAB DASHBOARD")
    border(ml, mr)
    row(f"OS:   {platform.system()} {platform.release()}")
    row(f"Host: {platform.node()}")
    row(f"Time: {datetime.now():%Y-%m-%d %H:%M:%S}")
    border(ml, mr)
    bar("CPU", cpu)
    bar("RAM", ram)
    bar("DISK", disk.used / disk.total * 100)
    row(f"TEMP  {temperature(unit)}")
    border(ml, mr)
    row("NETWORK (total since boot)")
    row(f"Received: {net.bytes_recv / 1024**2:,.1f} MB")
    row(f"Sent:     {net.bytes_sent / 1024**2:,.1f} MB")
    border(bl, br)


if __name__ == "__main__":
    main()
