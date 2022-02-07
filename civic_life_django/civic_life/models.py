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


class Legislation(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='legislations')
    title = models.TextField(blank=True)
    bill_number = models.CharField(max_length=50)
    summary = models.TextField(blank=True)
    url = models.TextField(blank=True)
    sponsor = models.CharField(max_length=200, default="no sponsor listed")
    cosponsor = models.CharField(
        max_length=200, default="no co-sponsor listed")
    date_introduced = models.CharField(max_length=100)

    def __str__(self):
        return self.bill_number


class Action(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='actions')
    date = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    completed = models.BooleanField()

    def __str__(self):
        return self.date
