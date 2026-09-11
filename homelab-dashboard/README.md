# 🖥️ HomeLab Dashboard

A simple Python terminal dashboard for monitoring a home server.

## Features

- CPU usage
- RAM usage
- Disk usage
- CPU temperature (when supported by the OS/hardware)
- Network traffic
- Operating system and hostname
- Current date and time
- ASCII progress bars

## Requirements

- Python 3.10+
- Linux, Windows or macOS
- `psutil`

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/homelab-dashboard.git
cd homelab-dashboard
```

Install the dependency:

```bash
pip install -r requirements.txt
```

Run:

```bash
python dashboard.py
```

## Example

```text
╔══════════════════════════════════════════════╗
║             HOMELAB DASHBOARD                ║
╠══════════════════════════════════════════════╣
║ CPU      ███████░░░░░░░░░░░░░░░░  28.0%      ║
║ RAM      █████████░░░░░░░░░░░░░░  36.0%      ║
║ DISK     ███████████████░░░░░░░░  61.0%      ║
║ TEMP     42.0°C                               ║
╚══════════════════════════════════════════════╝
```

## Project structure

```text
homelab-dashboard/
├── dashboard.py
├── requirements.txt
└── README.md
```

## Roadmap

- [ ] Web interface
- [ ] Docker container monitoring
- [ ] Automatic refresh
- [ ] Historical graphs
- [ ] Disk-by-disk monitoring
- [ ] Alerts when CPU/RAM/storage is too high
