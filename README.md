
# INFO8985 In-class Task 4

**Student:** Prem Chander J  
**Student ID:** 9015480

---

## Overview
This project demonstrates a complete observability pipeline using:
- **SigNoz** (Docker Compose) for telemetry storage and visualization
- **Kubernetes (k3s)** for local cluster orchestration
- **OpenTelemetry Collector** for trace/metrics/logs collection
- **Instrumented Flask app (rolldice.py)** for generating telemetry

## Architecture
```
Rolldice Flask App → OTEL Collector → SigNoz → Visualization
```

## Quick Start

### 1. Prerequisites
- Python 3.8+
- Docker & Docker Compose
- (Optional) k3s/k3d/kind for Kubernetes
- Ansible (for automation)

### 2. Setup
#### a. Clone the repository
```sh
git clone <your-repo-url>
cd INFO8985-Inclass-task-4
```

#### b. Set up Python environment
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### c. Start SigNoz (Docker Compose)
```sh
cd signoz/signoz/deploy/docker
sudo docker-compose up -d
```

#### d. Run the Flask app
```sh
cd /path/to/INFO8985-Inclass-task-4
python rolldice.py
```

### 3. Access Points
- **SigNoz UI:** [http://localhost:8081](http://localhost:8081)
- **Rolldice App:** [http://localhost:5000/rolldice](http://localhost:5000/rolldice)

### 4. Generate Telemetry
```sh
for i in {1..50}; do curl "http://localhost:5000/rolldice?player=alice"; done
```


### 5. View in SigNoz
- Open SigNoz UI
- Go to "Services" or "Traces"
- Look for `rolldice-app` service

### 6. Screenshots (add manually)
- _Screenshot: SigNoz UI main dashboard_
- _Screenshot: rolldice-app traces/metrics_

## Configuration
- Edit `rolldice.py` to set the correct OTLP exporter endpoint (see code comments)
- Edit `.gitignore` to avoid committing venv and other generated files

## Teardown
```sh
# Stop Flask app (Ctrl+C)
# Stop SigNoz
cd signoz/signoz/deploy/docker
sudo docker-compose down
```

## Files
- `rolldice.py` - Flask app with OpenTelemetry instrumentation
- `requirements.txt` - Python dependencies
- `signoz/` - SigNoz deployment files
- `up.yml`, `down.yml`, `rolldice.up.yml` - Ansible playbooks (optional)
- `.gitignore` - Excludes venv, pyc, etc.

## Screenshots
_Add screenshots of SigNoz UI and traces here if required._

---

**INFO8985 In-class Task 4 - Prem Chander J (9015480)**
