# Chapter 9: Monitoring Stack

## Prometheus + Grafana + Node Exporter

This project sets up a complete monitoring stack using Docker.

### Components

- **Prometheus** - Metrics collection (port 9090)
- **Grafana** - Visualization dashboard (port 3000)
- **Node Exporter** - System metrics exporter (port 9100)

### Screenshots

#### Grafana Dashboard (Node Exporter Full - ID: 1860)

![Dashboard](screenshots/Screenshot%202026-04-21%20232325)

#### PromQL Query - CPU Usage

![CPU Query](screenshots/Screenshot%202026-04-21%20231238)

#### Alert Rule - High CPU Usage (>80%)

![Alert Rule](screenshots/Screenshot%202026-04-21%20223401)

### How to Run

```bash
docker-compose up -d


# CPU Usage
100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# Memory Usage
(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100

# Disk Usage
(1 - (node_filesystem_avail_bytes{mountpoint="/"} / node_filesystem_size_bytes{mountpoint="/"})) * 100






