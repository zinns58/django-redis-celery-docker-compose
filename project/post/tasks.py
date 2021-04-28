import time
import random
from celery import shared_task

@shared_task(bind=True)
def debug_shared_task(self):
    rand_time = random.randint(1, 3)
    time.sleep(rand_time)
    print("debug shared task success : {} seconds".format(rand_time))