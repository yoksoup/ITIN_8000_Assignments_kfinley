"""
------------------------------------------------------------
This is the main model for the database that stores all the data
for the clubs in the project. Right now these field just hold data
and no processing is done in program.

If changes are made here, make sure to run:
> python manage.py makemigrations
> python manage.py migrate --run-syncdb

If problems still exists, delete the database that the system already has:
default is "db.squlite3" but you can find it in "settings.py"
------------------------------------------------------------
"""

from django.db import models
from django.urls import reverse

# Create your models here.
class Club(models.Model):
    title       = models.CharField(max_length=120) # max_length = required
    description = models.TextField(blank=True, null=True)
    meeting_info    = models.TextField(blank=True, null=True)
    person_in_charge= models.CharField(max_length=120) # max_length = required
    club_keywords   = models.CharField(max_length=120) # max_length = required
    featured    = models.BooleanField(default=False) # null=True, default=True

    # makes sure urls are dynamic
    # reverse lets you reverse back to page you were on before.
    def get_absolute_url(self):
        return reverse("clubs:club-detail", kwargs={"id": self.id})