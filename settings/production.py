from path import path

from settings.common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': SITE_ROOT / 'db/production.sqlite3',
    }
}

DEBUG = False
STATIC_ROOT = '/var/www/martinogden.me'
MEDIA_ROOT = STATIC_ROOT + '/media'
THUMBNAIL_DEBUG = True

