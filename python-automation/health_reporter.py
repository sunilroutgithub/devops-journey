#!/usr/bin/env python3

import psutil
import subprocess
import requests
import os
from datetime import datetime

# Environment variable for config
THRESHOLD = int(os.environ.get("HEALTH_THRESHOLD", "80"))

print("Running Health Reporter...")

report = []
report.append("=" * 50)
report.append(f"Server Health Report: {datetime.now()}")
report.append("=" * 50)

# 1 - CPU Usage
cpu = psutil.cpu_percent(interval=1)
report.append(f"\n--- CPU USAGE ---")
report.append(f"CPU: {cpu}%")

# 2 - Memory Usage
mem = psutil.virtual_memory()
mem_percent = mem.percent
report.append(f"\n--- MEMORY USAGE ---")
report.append(f"Memory: {mem_percent}%")

# 3 - Disk Usage
disk = psutil.disk_usage('/')
disk_percent = disk.percent
report.append(f"\n--- DISK USAGE ---")
report.append(f"Disk: {disk_percent}%")

# 4 - Read last 100 lines of syslog and count errors
report.append(f"\n--- SYSLOG ERRORS ---")
try:
    with open("/var/log/syslog", "r") as f:
        lines = f.readlines()
        last100 = lines[-100:]
        errors = [l for l in last100 if "ERROR" in l.upper()]
        report.append(f"Last 100 lines checked")
        report.append(f"ERROR lines found: {len(errors)}")
except FileNotFoundError:
    report.append("syslog not found")

# 5 - Check if cron service is running
report.append(f"\n--- SERVICE STATUS ---")
result = subprocess.run(
    ["systemctl", "is-active", "cron"],
    capture_output=True, text=True
)
status = result.stdout.strip()
report.append(f"cron service: {status}")

# 6 - Make GET request
report.append(f"\n--- API REQUEST ---")
try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    data = response.json()
    report.append(f"Title: {data['title']}")
except Exception as e:
    report.append(f"API request failed: {e}")

# 7 - ALERT check
report.append(f"\n--- ALERTS ---")
if disk_percent > THRESHOLD:
    report.append(f"ALERT: Disk usage is {disk_percent}%")
if mem_percent > THRESHOLD:
    report.append(f"ALERT: Memory usage is {mem_percent}%")
if disk_percent <= THRESHOLD and mem_percent <= THRESHOLD:
    report.append("All systems normal")

# 8 - Save report to file
timestamp = datetime.now().strftime("%Y%m%d_%H%M")
filename = f"health_report_{timestamp}.txt"
with open(filename, "w") as f:
    f.write("\n".join(report))

# Print report
print("\n".join(report))
print(f"\nReport saved: {filename}")
