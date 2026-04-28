![CI Pipeline](https://github.com/shamsnahidk/devops-fastapi-ci-cd/actions/workflows/ci.yml/badge.svg)

# DevOps FastAPI CI/CD Service

Production-style backend service demonstrating containerization, automated testing, and CI pipeline setup for reliable application delivery.

## What it does

- Exposes a FastAPI-based REST API
- Provides a `/health` endpoint for service monitoring
- Runs automated unit tests using pytest
- Builds and runs inside a Docker container
- Supports local execution using Docker Compose
- Uses GitHub Actions for CI automation
- Validates application changes on every push through an automated pipeline

## Tech Stack

- Python
- FastAPI
- Pytest
- Docker
- Docker Compose
- GitHub Actions

## Project Structure

```text
devops-fastapi-ci-cd/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── health.py
├── tests/
│   ├── __init__.py
│   └── test_health.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
└── README.md
```

## Setup and Run Locally

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Expected terminal output:

```text
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Run Tests

```bash
pytest
```

Expected output:

```text
1 passed
```

## API Execution Commands

### Root Endpoint

```bash
curl http://127.0.0.1:8000/
```

Expected output:

```json
{
  "message": "DevOps FastAPI service is running"
}
```

### Health Endpoint

```bash
curl http://127.0.0.1:8000/health
```

Expected output:

```json
{
  "status": "healthy",
  "service": "devops-fastapi-ci-cd",
  "timestamp": "2026-04-28T00:00:00+00:00"
}
```

## Run with Docker

Build the Docker image:

```bash
docker build -t devops-fastapi-ci-cd .
```

Expected output:

```text
Successfully built <image_id>
Successfully tagged devops-fastapi-ci-cd:latest
```

Run the container:

```bash
docker run -p 8000:8000 devops-fastapi-ci-cd
```

Then open:

```text
http://127.0.0.1:8000/health
```

Expected output:

```json
{
  "status": "healthy",
  "service": "devops-fastapi-ci-cd",
  "timestamp": "2026-04-28T00:00:00+00:00"
}
```

## Run with Docker Compose

```bash
docker compose up --build
```

Expected output:

```text
devops-fastapi-service  | Uvicorn running on http://0.0.0.0:8000
devops-fastapi-service  | Application startup complete.
```

Stop Docker Compose:

```text
Ctrl + C
```

## CI/CD Pipeline

The GitHub Actions workflow automatically runs on every push and pull request to the `main` branch.

Pipeline steps:

- Checkout repository
- Set up Python environment
- Install dependencies
- Run unit tests using pytest
- Build Docker image

Expected CI result:

```text
CI Pipeline: passed
Tests: passed
Docker build: passed
```

## Why This Project Matters

This project demonstrates practical DevOps engineering skills including backend service development, automated testing, Docker containerization, and CI pipeline setup. It shows how to build a service that is testable, reproducible, and ready for deployment workflows.

## Design Decisions

- **Framework**: FastAPI chosen for lightweight REST API development and built-in interactive documentation
- **Health Check Endpoint**: `/health` added to support service monitoring and validation
- **Testing**: Pytest used for simple, fast automated test execution
- **Containerization**: Docker used to create a consistent runtime environment across machines
- **Docker Compose**: Added to simplify local container execution
- **CI Tool**: GitHub Actions chosen for automated testing and Docker image validation on code changes
- **Repository Hygiene**: `.gitignore` and `.dockerignore` used to exclude virtual environments, cache files, and unnecessary build artifacts

## Limitations

- No production cloud deployment yet
- No database or persistent storage integration
- No authentication or authorization layer
- No centralized logging or monitoring dashboard
- Local Docker execution depends on Docker Desktop and WSL configuration on Windows

## Future Improvements

- Deploy to a cloud platform such as Render, AWS, or Azure
- Add structured logging for better observability
- Add monitoring with Prometheus and Grafana
- Integrate PostgreSQL for persistent data storage
- Add environment configuration using `.env`
- Extend CI/CD pipeline to include automated deployment
- Add security scanning for dependencies and Docker images
