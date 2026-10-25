# HomeLab Dashboard

A one-shot terminal dashboard for CPU, memory, system drive, temperature, network totals, host, and time.

## Download

Use **Code → Download ZIP** on [GitHub](https://github.com/cc-codex44/homelab-dashboard), then extract it; or clone it:

```bash
git clone https://github.com/cc-codex44/homelab-dashboard.git
cd homelab-dashboard
```

If you downloaded a ZIP, open a terminal in the extracted `homelab-dashboard` folder instead.

## Install and run

Requires Python 3.10 or newer on Windows, Linux, or macOS.

```bash
python -m pip install -r requirements.txt
python dashboard.py
```

On systems where Python is called `python3`, replace `python` with `python3` in both commands. The dashboard prints one snapshot and exits.

Temperature shows `N/A` when the OS or hardware does not expose a sensor. Disk usage is for the system drive; network totals are cumulative counters since boot. The display uses ASCII when the terminal cannot print box-drawing characters.
