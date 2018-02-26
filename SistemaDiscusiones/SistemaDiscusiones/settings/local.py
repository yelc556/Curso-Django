from .base import *

DEBUG = True

ALLOWED_HOSTS = []



# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Discusionesdb',
        'USER': 'yelc',
        'PASSWORD': 'pass123',
        'HOST': 'Localhost',
        'PORT': '5432'
    }
}




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
