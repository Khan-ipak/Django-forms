import os

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'news_db',       # Имя базы данных
        'USER': 'postgres',       # Пользователь
        'PASSWORD': 'yourpassword',  # Пароль
        'HOST': 'localhost',      # Адрес сервера
        'PORT': '5432',           # Порт PostgreSQL
    }
}
