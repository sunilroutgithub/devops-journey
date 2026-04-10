# DevOps Journey

My DevOps learning projects from scratch.

## Chapter 1 — Linux: Health Monitor Script

A bash script that monitors Linux system health automatically.

### What it does
- Checks disk usage
- Checks available memory
- Lists top 5 CPU processes
- Checks port 8080 status
- Saves timestamped log files

### How to run
chmod +x health_monitor.sh
./health_monitor.sh

### Cron Schedule
Runs every 5 minutes:
*/5 * * * * /home/dev/health_monitor.sh

## Chapter 2 — Git and GitHub
- Created GitHub repo
- Cloned to WSL
- Created branch
- Pushed code
- Opened Pull Request
- Merged to main
