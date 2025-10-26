# travel_app/travel_app/celery.py

import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_app.settings')

app = Celery('travel_app')

# Load task configuration from Django settings, using 'CELERY' prefix for keys.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks from all installed apps (looks for tasks.py files).
app.autodiscover_tasks()