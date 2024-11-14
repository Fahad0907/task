import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

app.config_from_object('django.conf:settings',
                       namespace='CELERY')

app.autodiscover_tasks()

CELERY_BEAT_SCHEDULE = {
    'task-every-30-minute': {
        'task': 'AuthorBook.task.makeArchive',
        'schudule': crontab(minute='*/30')
    }
}