"""
WSGI config for inventory_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
import sys

# Add your project directory to the Python path
project_home = '/home/bryanbudah/inventory_api'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'inventory_api.settings'

# Activate your virtual environment
activate_env = '/home/bryanbudah/inventory_api/venv/bin/activate_this.py'
with open(activate_env) as f:
    exec(f.read(), {'__file__': activate_env})

# Import Django's WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
