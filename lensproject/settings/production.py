from .common import *

SECRET_KEY = os.environ.get('DJANGO_LENS_SECRET_KEY')

ALLOWED_HOSTS = ['lens.lianch.com',]
DEBUG = False