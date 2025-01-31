from .settings import *

DEBUG = True

# Использование SQLite для локальной разработки
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Конфигурация сервера электронной почты
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'ingopogreb@gmail.com'
# EMAIL_HOST_PASSWORD = ''
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

