from django.db import models
from django.utils import timezone

class Parcel(models.Model):
    tracking_number = models.CharField(max_length=100, unique=True)
    sender = models.CharField(max_length=255)
    recipient = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    received_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.tracking_number
