
from celery import Celery
from celery.schedules import crontab

from .config import settings

# Initialize the Celery application
celery_app = Celery(
    "tasks",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
    include=['app.tasks']  # Points to the module where tasks are defined
)

celery_app.conf.update(
    task_track_started=True,
)

# Define a periodic task schedule
celery_app.conf.beat_schedule = {
    'check-expired-subscriptions-daily': {
        'task': 'app.tasks.check_expired_subscriptions',
        'schedule': crontab(hour=0, minute=5),  # Runs daily at 00:05 AM
    },
}

# Optional: A simple task for testing
@celery_app.task
def add(x, y):
    return x + y
