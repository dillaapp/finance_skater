from datetime import datetime

from django.db import models


# Create your models here.
class FinAdvisors(models.Model):
    id = models.AutoField(primary_key=True)
    fin_advisor_name = models.CharField(max_length=200)
    fin_advisor_username = models.CharField(max_length=200)
    bio_statement = models.TextField(max_length=280)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.fin_advisor_username


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    fin_advisor_username = models.TextField(max_length=150)
    first_name = models.TextField(max_length=150)
    email = models.TextField(max_length=150)
    day_and_time = models.TextField(max_length=150)
    location = models.TextField(max_length=280)
    topic = models.TextField(max_length=280)
    booking_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.email
