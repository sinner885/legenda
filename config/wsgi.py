"""
WSGI config for infopogreb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from environ import Env

env = Env()
env.read_env()

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'infopogreb.settings')
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", env.str("DJANGO_SETTINGS_MODULE", "config.setting")
)

application = get_wsgi_application()
