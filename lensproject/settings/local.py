from .common import *

DEBUG = True
SECRET_KEY = os.environ.get('DJANGO_LENS_SECRET_KEY', default='i2k%m-808v3_)^h7975iw4v&fl5chq41^19j@u+b*vx7dvw*q$') 
# debug toolbar 
INTERNAL_IPS = ['127.0.0.1']
JQUERY_URL = ''
ALLOWED_HOSTS = ['*',]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INSTALLED_APPS += [
    'debug_toolbar',
    'sslserver',
]
