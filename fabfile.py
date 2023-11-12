import os

from fabric.api import env, run, cd, prefix, sudo, put
import dotenv
dotenv.load_dotenv()


local_project_root = os.path.dirname(__file__)
remote_project_root = '/opt/usb-memory-formatter'

env.hosts = [os.environ['DEPLOY_TARGET_HOSTNAME']]
env.user = os.environ['DEPLOY_TARGET_USERNAME']


def deploy():
    run(f'sudo mkdir -p {remote_project_root}')
    run(f'sudo chown {env.user} {remote_project_root}')
    with cd(remote_project_root):

        put('app/50-format-usb-memory.rules', '/etc/udev/rules.d/50-format-usb-memory.rules', use_sudo=True)
        put('app/log.sh', 'log.sh')
        sudo('service udev restart')
