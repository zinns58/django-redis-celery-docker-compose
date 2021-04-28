from .base import *
from decouple import config

# DEBUG MODE
DEBUG = False

# WSGI application
WSGI_APPLICATION = 'config.wsgi.deploy.application'

# allowed hosts
ALLOWED_HOSTS = ['*']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# remote Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'HOST': config('DB_HOST'),
#         'PORT': config('DB_PORT'),
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#     }
# }

# static file dirs
STATIC_ROOT = './static/'
MEDIA_ROOT = './media/'

# Celery
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER", "redis://redis:6379/0")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_BROKER", "redis://redis:6379/0")
