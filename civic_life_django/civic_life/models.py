from operator import mod
from sre_parse import State
from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_URL = models.TextField(blank=True)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=5)
    zip_code = models.IntegerField()

    def __str__(self):
        return self.first_name
