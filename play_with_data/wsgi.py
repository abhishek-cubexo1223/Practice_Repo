"""
WSGI config for play_with_data project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
# this comment is add for main testing
from django.core.wsgi import get_wsgi_application
# this commit is a new branch
# this commit is a new branch
# this commit is a new branch
# this commit is a new branch
# this commit is a new branch
# this commit is a new branch

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'play_with_data.settings')

application = get_wsgi_application()
