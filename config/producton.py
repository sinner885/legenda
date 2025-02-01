from .settings import *

DEBUG = False
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('NAME'),
        'USER': env.str('USER'),
        'PASSWORD': env.str('PASSWORD'),
        'HOST': env.str('HOST'),
        'PORT': env.int('PORT')
    }
}