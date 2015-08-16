from fabric.api import require, put, cd, task
from fabric.colors import red, green
from .conf import *
from sys import exit

@task(default=True)
def main(*args, **kwargs):
    """
    updates the project locals.py to new settings
    """
    e = dict()
    if 'local' in args or 'dev' in args or len(args) == 0:
        e = globals()['local_env']()
    elif 'stage' in args or 'staging' in args:
        e = globals()['staging_env']()
    elif 'live' in args or 'web' in args:
        e = globals()['live_env']()
    else:
        exit(red('Invalid Argument for task'))
    update_settings(e)


def update_settings(environment):
    with cd(environment.project_root):
        environment.run('cp conf/envs/%(conf_path)s/locals.py conf/settings/locals.py' % environment)
        exit(green('Local Environment Settings are updated successfully'))

__all__ = ['main']
