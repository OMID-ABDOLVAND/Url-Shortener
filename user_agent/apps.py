import os
from django.apps import AppConfig
from django.conf import settings

from core.settings import BASE_DIR


class UserAgentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_agent'
    path = BASE_DIR / 'user_agent'
