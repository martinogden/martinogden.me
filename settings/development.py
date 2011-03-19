from path import path

from settings.common import *

TEMPLATE_DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': SITE_ROOT / 'db/development.sqlite3',
    }
}

MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS += ('debug_toolbar',)
INTERNAL_IPS = ('127.0.0.1', '0.0.0.0')
DEBUG_TOOLBAR_CONFIG = {"INTERCEPT_REDIRECTS": False}