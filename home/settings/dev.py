from home.settings.prod import *

DEBUG = True

SECRET_KEY = '42'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'home',
        'USER': 'home_user',
        'PASSWORD': 'home_password',
        'HOST': 'db',
        'PORT': '3306',
    }
}