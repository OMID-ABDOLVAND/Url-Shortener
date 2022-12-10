import os

from django.apps import AppConfig

from core.settings import BASE_DIR


class UrlshourterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'urlshourter'
    path = os.path.join(BASE_DIR, 'urlshourter')