from django.db import models

# addressbook models.

from django.db import models
class Entry(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    mobile = models.CharField(max_length=30)
    address = models.CharField(max_length=80)
    email = models.EmailField()

