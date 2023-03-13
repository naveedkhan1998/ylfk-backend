"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os,sys
sys.path.append('/var/www/YLFK-BACKEND')
sys.path.append('/var/www/YLFK-BACKEND/venv/lib/python3.10/site-packages')
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

application = get_wsgi_application()