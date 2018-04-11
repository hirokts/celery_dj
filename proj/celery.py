from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from celery.utils.log import get_task_logger
from django.conf import settings

logger = get_task_logger(__name__)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    logger.info('Request: {0!r}'.format(self.request))


# app.conf.beat_schedule = {
#     'add-every-10-seconds': {
#         'task': 'demoapp.tasks.add',
#         'schedule': 10.0,
#         'args': (16, 16)
#     },
# }