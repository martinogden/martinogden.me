from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

from django.conf import settings


env.hosts = ['blist']

def deploy():
    tar = '/tmp/me.tar.gz'
    local('scp %s *' % tar)
    local('scp %s blist:/tmp/' % tar)
    run('tar xzfv %s /var/project/' % tar)
