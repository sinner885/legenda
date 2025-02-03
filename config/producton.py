from .settings import *
from environ import Env

env = Env()
env.read_env()

# print(f"DATABASES config: {env.str('NAME')}, {env.str('USER')}, {env.str('HOST')}, {env.int('PORT')}")

print(f"Используется файл настроек: {os.environ.get('DJANGO_SETTINGS_MODULE')}")
try:
    print(f"DATABASES config: {env.str('NAME')}, {env.str('USER')}, {env.str('HOST')}, {env.int('PORT')}")
except Exception as e:
    print(f"Ошибка при загрузке переменных окружения: {e}")
DEBUG = env.bool('DEBUG')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])
print(f"ALLOWED_HOSTS: {ALLOWED_HOSTS}")
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('NAME'),
        'USER': env.str('USER'),
        'PASSWORD': env.str('PASSWORD'),
        'HOST': env.str('HOST'),
        'PORT': env.int('PORT'),
    }
}
