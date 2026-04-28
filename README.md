# DevOps FastAPI CI/CD Project

A Dockerized FastAPI backend service with automated testing and CI pipeline using GitHub Actions.

## Features
- FastAPI REST API
- Health check endpoint
- Unit testing with pytest
- Docker containerization
- Docker Compose support
- GitHub Actions CI pipeline
- Automated test and Docker build workflow

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
│   ├── main.py
│   └── health.py
├── tests/
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
## Run Locally
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
## Open:
``` Text
http://127.0.0.1:8000/docs
```
## Run Tests
```bash
pytest
```
## Run with Docker
```bash
docker build -t devops-fastapi-ci-cd .
docker run -p 8000:8000 devops-fastapi-ci-cd
```
## Run with Docker Compose
```bash
docker compose up --build
```
## API Endpoints
GET /
GET /health

## Example response:
```json
{
  "status": "healthy",
  "service": "devops-fastapi-ci-cd"
}
```
## CI/CD Pipeline
The GitHub Actions workflow automatically runs on every push to the main branch.

Pipeline Steps:
Checkout code
Install dependencies
Run unit tests (pytest)
Build Docker image

This ensures that:

Code is always tested
Builds are reproducible
Deployment artifacts are validated

## What This Project Demonstrates
Backend service development using FastAPI
Writing and running automated tests
Containerizing applications with Docker
Setting up CI pipelines with GitHub Actions
Ensuring code reliability through automation
Building deployment-ready backend services

## Future Improvements
Deploy to cloud platform (Render / AWS / Azure)
Add logging and monitoring
Add environment configuration support
Integrate database service

## Why This Project Matters
This project showcases practical DevOps skills including testing, automation, and containerization. It demonstrates the ability to build and ship backend systems that are reliable, reproducible, and ready for deployment.





