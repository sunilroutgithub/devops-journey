#!/bin/bash
TIMESTAMP=$(date +"%Y%m%d_%H%M")
LOGFILE="/home/$USER/logs/health_$TIMESTAMP.log"
mkdir -p /home/$USER/logs
echo "=============================" >> $LOGFILE
echo "Health Check: $(date)" >> $LOGFILE
echo "=============================" >> $LOGFILE
echo "--- DISK USAGE ---" >> $LOGFILE
df -h >> $LOGFILE
echo "--- MEMORY USAGE ---" >> $LOGFILE
free -h >> $LOGFILE
echo "--- TOP 5 CPU PROCESSES ---" >> $LOGFILE
ps aux --sort=-%cpu | head -6 >> $LOGFILE
echo "--- PORT 8080 STATUS ---" >> $LOGFILE
ss -tulnp | grep 8080 >> $LOGFILE || echo "Port 8080 not in use" >> $LOGFILE
echo "Log saved: $LOGFILE"
