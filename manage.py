#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    try:
        from jamesbeedyblog.settings import local
        settings_module = "jamesbeedyblog.settings.local"
    except ImportError:
        settings_module = "jamesbeedyblog.settings"

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
