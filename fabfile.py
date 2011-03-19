from __future__ import with_statement
import os

from fabric.api import *
from fabric.contrib.console import confirm

from django.conf import settings

env.user = 'root'
env.hosts = ['109.169.46.254']
env.root = '/var/virtualenvs/martinogden.me'
env.directory = '%s/project/' % env.root


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

def virtualenv(command):
    """
    Run a command in the virtualenv. This prefixes the command with the source
    command.
    Usage:
        virtualenv('pip install django')
        
    Adapted from: http://stackoverflow.com/questions/1180411/activate-a-virtualenv-via-fabric-as-deploy-user/3403558#3403558
    """
    source = 'source %s/bin/activate && ' % env.root
    with cd(env.directory):
        run(source + command)
 
def django(command):
    virtualenv('django-admin.py %s' % command)

def touch():
    run('service apache2 graceful')

def deploy():
    run(' rm -R %s' % env.directory)
    _put_dir(settings.PROJECT_ROOT, env.directory)
    touch()

def syncdb():
    django('syncdb')

def migrate(app):
    django('migrate %s' % app)