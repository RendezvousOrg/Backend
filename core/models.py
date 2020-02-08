from django.db import models
from django.contrib.auth.models import User

class Plan(models.Model):
    creator = models.CharField(max_length=105)
    location = models.CharField(max_length=105)
    datetime = models.CharField(max_length=105)
    activity = models.TextField()
    attendees = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.datetime} with {self.creator}"