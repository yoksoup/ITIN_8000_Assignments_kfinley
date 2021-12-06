"""
------------------------------------------------------------
created by Kyle Finley for ITIN 8000 Final Project
------------------------------------------------------------
This is the main file for the Scout Web server.

1.Setup:
a. Make sure Django is installed. Go to src folder and:
> pip install django
> python manage.py makemigrations
> python manage.py migrate --run-syncdb

b. Then run this with:
> python manage.py runserver

2. Description: The main tasks of the program is to create objects for a database,
display objects from the database, and display this on a webserver. This program does that with
limited displayed options as the focus was on functionally.

3. Assets: Creates a webserver with Home, Club list, Create, hidden delete function(not fully functional), and an admin page.
home page is:
127.0.0.1:8000/admin

4. Problem solving: If there are database issues with it not finding the table
run:
> python manage.py makemigrations
> python manage.py migrate --run-syncdb

5. Admin: To access admin you have to:
> python manage.py createsuperuser
Then login to the admin page
127.0.0.1:8000/admin

------------------------------------------------------------
Templates for this code is from freeCodeCamp.org
https://www.youtube.com/watch?v=F5mRW0jo-U4
Python Django Web Framework - Full Course for Beginners
------------------------------------------------------------
"""

#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scout.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
