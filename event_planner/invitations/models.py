from django.db import models
from django.contrib.auth.models import User
from events.models import Event
from django.utils import timezone


class Invitations(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    STATUS_CHOICES = [
        ("invited", "Invited"),
        ("accepted", "Accepted"),
        ("declined", "Declined"),
    ]
    status = models.CharField(max_length=20, blank="true", default="Invited", choices=STATUS_CHOICES)

    def set_status(self, status):
        if status in self.STATUS_CHOICES:
            self.status = status
        else:
            raise ValueError("Invalid status value")
        
