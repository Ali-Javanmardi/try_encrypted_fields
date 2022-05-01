#!/usr/bin/env python
import os
import sys

import warnings
from optparse import OptionParser

import django
from django.conf import settings
from django.core.management import call_command

def runtests(test_path='enc_field'):
    if not settings.configured:
        # Choose database for settings
        test_db = os.getenv('DB', 'sqlite')
        test_db_host = os.getenv('DB_HOST', 'localhost')
        DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': ':memory:'}}


        # Configure test environment
        settings.configure(
            DATABASES=DATABASES,
            INSTALLED_APPS=(
                'django.contrib.contenttypes',
                'django.contrib.auth',
                'enc_field.apps.EncFieldConfig',
            ),
            ROOT_URLCONF=None, 
            LANGUAGES=(('en', 'English'),),
            MIDDLEWARE_CLASSES=(),
            SECRET_KEY = 'fake-key',
            SALT_KEY = '0123456789abcdefghijklmnopqrstuvwxyz',
        )
        
    django.setup()
    warnings.simplefilter('always', DeprecationWarning)
    failures = call_command('test', test_path, interactive=False, failfast=False, verbosity=2)

    sys.exit(bool(failures))


if __name__ == '__main__':
    parser = OptionParser()

    (options, args) = parser.parse_args()
    runtests(*args)

