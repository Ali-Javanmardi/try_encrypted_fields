#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "migrations_settings")
    from django.core.management import execute_from_command_line
    args = sys.argv + ["makemigrations", "enc_field"]
    execute_from_command_line(args)