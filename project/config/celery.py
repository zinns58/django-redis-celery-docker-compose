import os
import time
import random

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.deploy')

app = Celery('celery_worker')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    rand_time = random.randint(1, 3)
    time.sleep(rand_time)
    print("debug task success : {} seconds".format(rand_time))