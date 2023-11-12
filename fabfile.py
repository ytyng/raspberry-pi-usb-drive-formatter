import os

from fabric.api import env, run, cd, prefix, sudo, put, lcd
import dotenv
dotenv.load_dotenv()


local_project_root = os.path.dirname(__file__)
remote_project_root = '/opt/usb-storage-formatter'

env.hosts = [os.environ['DEPLOY_TARGET_HOSTNAME']]
env.user = os.environ['DEPLOY_TARGET_USERNAME']


def deploy():
    with lcd(local_project_root):
        run(f'sudo mkdir -p {remote_project_root}')
        run(f'sudo chown {env.user} {remote_project_root}')
        with cd(remote_project_root):

            put('app/50-format-usb-storage.rules',
                '/etc/udev/rules.d/50-format-usb-storage.rules',
                use_sudo=True)
            put('app/on-usb-plugged-in.sh', 'on-usb-plugged-in.sh', mode='0755')
            put('app/log.sh', 'log.sh', mode='0755')
            sudo('service udev restart')


def tail_log():
    run('tail -f /var/log/usb-storage-formatter/usb-storage-formatter.log '
        '/var/log/syslog')
