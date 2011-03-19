from __future__ import with_statement
import os

from fabric.api import *
from fabric.contrib.console import confirm

from django.conf import settings

env.user = 'root'
env.hosts = ['109.169.46.254']
env.root = '/var/virtualenvs/martinogden.me/project/'

def _put_dir(local_dir, remote_dir):
    """Copy a local directory to a remote one, using tar and put. Silently
    overwrites remote directory if it exists, creates it if it does not
    exist."""
    local_tgz = "/tmp/fabtemp.tgz"
    remote_tgz = os.path.basename(local_dir) + ".tgz"
    local('tar -C "{0}" -czf "{1}" .'.format(local_dir, local_tgz))
    put(local_tgz, remote_tgz)
    local('rm -f "{0}"'.format(local_tgz))
    run('rm -Rf "{0}"; mkdir "{0}"; tar -C "{0}" -xzf "{1}" && rm -f "{1}"'\
        .format(remote_dir, remote_tgz))

def deploy():
    _put_dir(settings.PROJECT_ROOT, env.root)
