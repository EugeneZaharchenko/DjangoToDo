from django.db import models
from datetime import datetime


class Task(models.Model):
    title = models.CharField(max_length=150)
    details = models.TextField(blank=True)
    created = models.DateTimeField(default=datetime.now, blank=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
