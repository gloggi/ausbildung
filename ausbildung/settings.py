import os
import sys
import dj_database_url

_ = lambda x: x

WEBAPP_DIR = os.path.dirname(os.path.abspath(__file__))
APP_BASEDIR = os.path.abspath(os.path.join(WEBAPP_DIR, os.path.pardir))
DEBUG = any((cmd in sys.argv for cmd in (
    'runserver', 'shell', 'dbshell', 'sql', 'sqlall')))
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Gloggi Admin', 'admin@gloggi.ch'),
)

MANAGERS = ADMINS

DEV_DB = os.path.join(APP_BASEDIR, 'dev.db')

DATABASES = {'default': dj_database_url.config(default='sqlite:///%s' % DEV_DB)}

TIME_ZONE = 'Europe/Zurich'

LANGUAGE_CODE = 'de-CH'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = False

LANGUAGES = (('de', _('German')),)

AWS_ACCESS_KEY_ID = os.environ.get('S3_KEY','')
AWS_SECRET_ACCESS_KEY = os.environ.get('S3_SECRET','')
AWS_STORAGE_BUCKET_NAME = 'gloggiausbildung'

if DEBUG:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211'
        }
    }
else:
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    CACHES = {
        'default': {
            'BACKEND': 'django_pylibmc.memcached.PyLibMCCache'
        }
    }

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

MEDIA_ROOT = os.path.join(APP_BASEDIR, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(APP_BASEDIR, 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(APP_BASEDIR, 'ausbildung', 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ausbildung.urls'

WSGI_APPLICATION = 'ausbildung.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(APP_BASEDIR, 'ausbildung', 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    'feincms',
    'feincms.module.page',
    'feincms.module.medialibrary',
    'fhadmin',
    'tinymce',
    'south',
    'gunicorn',
    'django_countries',

    'ausbildung',
    'ausbildung.kurse',
)

FEINCMS_RICHTEXT_INIT_CONTEXT = {
    'TINYMCE_JS_URL': STATIC_URL + '/tiny_mce/tiny_mce.js',
}

from fhadmin import FHADMIN_GROUPS_REMAINING
_ = lambda x: x

FHADMIN_GROUPS_CONFIG = [
    (_('Main content'), {
        'apps': ('page', 'medialibrary', 'blog'),
        }),
    (_('Modules'), {
        'apps': ('links', FHADMIN_GROUPS_REMAINING),
        }),
    (_('Preferences'), {
        'apps': ('auth', 'rosetta', 'external', 'sites'),
        }),
    ]
