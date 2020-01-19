from django.db import models

class Plan(models.Model):
    creator = models.CharField(max_length=105)
    location = models.CharField(max_length=105)
    datetime = models.DateTimeField()
    activity = models.TextField()

    def __str__(self):
        return f"{self.datetime} with {self.creator}"