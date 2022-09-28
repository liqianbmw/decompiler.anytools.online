from .base import *
# DEBUG=False
DEBUG=True
ALLOWED_HOSTS = ['*'] 
JADX_HOME = 'sh /www/wwwroot/tempfile/jadx/bin/jadx -d '
APKTOOL_HOME="/www/wwwroot/tempfile/apktool_2.6.1.jar";
FILE_PATH = "/www/wwwroot/tempfile";
INTERNAL_IPS = ['127.0.0.1', ] #debug_toolbar

# STATICFILES_DIRS = [ os.path.join(CORE_DIR, "../static/"),]
STATICFILES_DIRS = [ "/www/wwwroot/decompiler.anytools.online/website/static"]
# STATIC_URL = '/static/'
STATIC_URL = '/www/wwwroot/decompiler.anytools.online/website/static'
# STATIC_ROOT = os.path.join(CORE_DIR, "static")
STATIC_ROOT = "/www/wwwroot/decompiler.anytools.online/static";