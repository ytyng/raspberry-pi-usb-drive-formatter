import os

import dotenv
from fabric.api import cd, env, lcd, local, prefix, put, run, sudo

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

            put(
                'app/50-format-usb-storage.rules',
                '/etc/udev/rules.d/50-format-usb-storage.rules',
                use_sudo=True,
            )
            put(
                'app/on-usb-plugged-in.sh', 'on-usb-plugged-in.sh', mode='0755'
            )
            put('app/log.sh', 'log.sh', mode='0755')
            put(
                'app/format_usb_storage.py',
                'format_usb_storage.py',
                mode='0755',
            )
            put(
                'app/user_interfaces.py',
                'user_interfaces.py',
                mode='0755',
            )
            put(
                '.env',
                '.env',
                mode='0755',
            )
            sudo('service udev restart')


def ssh():
    local(f'ssh {env.user}@{env.hosts[0]}')


def dev():
    # test_script_name = 'beep_test.py'
    test_script_name = 'led_test.py'
    with lcd(local_project_root):
        with cd(remote_project_root):
            put(f'dev/{test_script_name}', test_script_name, mode='0755')
            run(f'./{test_script_name}')


def ui_test():
    with lcd(local_project_root):
        with cd(remote_project_root):
            put(
                'app/user_interfaces.py',
                'user_interfaces.py',
                mode='0755',
            )
            put(
                '.env',
                '.env',
                mode='0755',
            )
            run(f'set -a && source .env && set +a && ./user_interfaces.py')


def tail_log():
    run(
        'tail -f /var/log/usb-storage-formatter/usb-storage-formatter.log '
        '/var/log/syslog'
    )
