#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django module can't be found. This is required in order to be able to run this app."
            "Also make sure that the virtual environment is already set. This can be done using cmd or powershell prompting"
            "it inside the main folder which contains all the required attributes of Django."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
