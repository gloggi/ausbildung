from fabric.api import *

env.forward_agent = True
env.hosts = ['admin@srv.aure4.ch']

@task
def deploy():
    local('git push origin')
    with cd('/var/www/aure4'):
        run('git pull')
        run('find . -name "*.pyc" -delete')
        run('venv/bin/pip install -r requirements.txt')
        run('venv/bin/python manage.py migrate')
        run('venv/bin/python manage.py syncdb')
        run('venv/bin/python manage.py collectstatic --noinput')
        run('sudo service aure4 restart')