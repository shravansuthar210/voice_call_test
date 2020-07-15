from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class voice_call_array(models.Model):
    sender_number=models.IntegerField(blank=False)
    receiver_numer=models.IntegerField(blank=False)
    voice_array=ArrayField(models.IntegerField())