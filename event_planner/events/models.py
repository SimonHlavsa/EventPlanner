from django.db import models
from django.utils import timezone


class Event(models.Model):
    name = models.CharField(max_length=250, default='', blank=True)
    location = models.CharField(max_length=250, default='', blank=True)
    description = models.CharField(max_length=500, default='', blank=True)
    event_start = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

