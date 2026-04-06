import datetime

from django.db import models
from django.utils import timezone
class Entry(models.Model):
    entry_summary = models.CharField(max_length = 200)
    entry_details = models.CharField()
    entry_date = models.DateTimeField('date published')

# Create your models here.
