![CI Pipeline](https://github.com/shamsnahidk/devops-fastapi-ci-cd/actions/workflows/ci.yml/badge.svg)

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