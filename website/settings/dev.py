from .base import *
# DEBUG=False
INTERNAL_IPS = ['127.0.0.1', ]#debug_toolbar
DEBUG=True
ALLOWED_HOSTS = ['*']
JADX_HOME = 'jadx -d '
APKTOOL_HOME="/Users/qianli/workspace/python/www/tools/apktool_2.6.1.jar";
FILE_PATH = "/Users/qianli/workspace/python/www/tools";
DOWN_FILE ="/Users/qianli/workspace/python/www/tools/down"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(CORE_DIR, '/static/')
STATIC_URL = os.path.join(CORE_DIR, '/static/')
STATICFILES_DIRS = [ os.path.join(BASE_DIR, "static/"),]
# STATIC_ROOT = "/Users/qianli/workspace/python/www/tools/static/"