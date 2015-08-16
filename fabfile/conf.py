import os
from fabric.api import env, run, local as lrun

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

LOCAL_PROJECT_PATH = BASE_DIR
LOCAL_ENVIRONMENT_PATH = ''

STAGING_KEY = ''
STAGING_HOSTS = ['stage.adomattic.com', ]

LIVE_KEY = ''
LIVE_HOSTS = []

# defining development environment
def local_env():
    """
    Environment settings for local.
    Usage:
         fab local <task>
    """
    env.run = lrun
    env.name = 'dev'
    env.conf_path = 'dev'
    env.project_root = LOCAL_PROJECT_PATH
    env.hosts = ['localhost']
    env.branch = 'develop'
    env.venv_root = LOCAL_ENVIRONMENT_PATH
    env.venv = 'source %(venv_root)sbin/activate && ' % env
    return env


def staging_env():
    env.run = run
    env.name = 'stage'
    env.conf_path = 'stage'
    env.project_root = '/srv/%(name)s/' % env
    env.hosts = STAGING_HOSTS
    env.host_string = STAGING_HOSTS[0]
    env.user = 'root'
    env.key_filename = STAGING_KEY
    # env.no_keys = True
    # env.use_ssh_config = False
    env.branch = 'develop'
    env.venv_root = '/srv/%(name)s/' % env
    env.venv = 'source /srv/%(name)s/bin/activate && ' % env
    return env


def live_env():
    env.run = run
    env.name = 'live'
    env.conf_path = 'live'
    env.project_root = '/srv/%(name)s/' % env
    env.hosts = LIVE_HOSTS
    env.host_string = LIVE_HOSTS[0]
    env.user = 'root'
    env.key_filename = LIVE_KEY
    # env.no_keys = True
    # env.use_ssh_config = False
    env.branch = 'develop'
    env.venv_root = '/srv/%(name)s/' % env
    env.venv = 'source /srv/%(name)s/bin/activate && ' % env
    return env
