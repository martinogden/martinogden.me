import os
import sys
import site

site_root = '/home/martin/.virtualenvs/martinogden.me'
site.addsitedir(site_root + '/lib/python2.6/site-packages/')

activate_this = site_root + '/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

path = '/home/martin/sites/martinogden.me/project'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.production'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
