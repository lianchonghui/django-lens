# coding:utf-8

from fabric.api import env,run
from fabric.operations import sudo

GIT_REPO = 'https://github.com/lianchonghui/django-lens.git'

env.user = 'lianch'

env.hosts = ['lens.lianch.com',]
env.port = '22'

def deploy():
    source_folder = '/home/lianch/sites/lianch.com/django-lens'
    sudo('systemctl stop gunicorn-lens.lianch.com')

    run('cd %s && git pull' % source_folder)
    run('cd {} && cp ./lensproject/settings/production.py ./lensproject/settings/__init__.py'.format(source_folder))
    run("""
        cd {} &&
        ../env/bin/pip install -r ./requirements/production.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    sudo('systemctl start gunicorn-lens.lianch.com')
    #sudo('service nginx reload')
