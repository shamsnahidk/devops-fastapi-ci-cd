from datetime import datetime, timezone

def get_health_status():
    return {
        "status": "healthy",
        "service": "devops-fastapi-ci-cd",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }