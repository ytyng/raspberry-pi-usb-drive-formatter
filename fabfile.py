import os

import dotenv
from fabric.api import cd, env, lcd, local, prefix, put, run, sudo

dotenv.load_dotenv()


local_project_root = os.path.dirname(__file__)
remote_project_root = '/opt/usb-storage-formatter'

env.hosts = [os.environ['DEPLOY_TARGET_HOSTNAME']]
env.user = os.environ['DEPLOY_TARGET_USERNAME']

deploy_files = [
    'app/on-usb-plugged-in.sh',
    'app/log.sh',
    'app/format_usb_storage.py',
    'app/user_interfaces.py',
    'app/power_on_beep.py',
    '.env',
]


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

            for file in deploy_files:
                put(file, os.path.basename(file), mode='0755')

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
            for file in [
                'app/user_interfaces.py',
                '.env',
            ]:
                put(file, os.path.basename(file), mode='0755')
            run(f'set -a && source .env && set +a && ./user_interfaces.py')


def power_on_beep_test():
    with lcd(local_project_root):
        with cd(remote_project_root):
            for file in [
                'app/power_on_beep.py',
                '.env',
            ]:
                put(file, os.path.basename(file), mode='0755')
            run(f'set -a && source .env && set +a && ./power_on_beep.py')


def tail_log():
    run(
        'tail -f /var/log/usb-storage-formatter/usb-storage-formatter.log '
        '/var/log/syslog'
    )
