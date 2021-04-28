from django.http import JsonResponse
from config.celery import debug_task
from .tasks import debug_shared_task


def index(request):
    # async
    debug_task.delay()
    debug_shared_task.delay()

    return JsonResponse({
        'title': 'Hello Celery!!',
        'content': [
            'python',
            'django',
            'redis'
            'celery',
        ]
    }, json_dumps_params = {'ensure_ascii': True})