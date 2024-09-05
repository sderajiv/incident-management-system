from django.db import models
from django_countries.fields import CountryField
# import datetime, random
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mobile = models.BigIntegerField(unique=True)
    add = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    # country = CountryField()
    country = models.CharField(max_length=100)
    pin = models.CharField(max_length=6)

class Incident(models.Model):
    identity_field = [('Enterprise', 'Enterprise'),('Government', 'Government')]
    p_choice = [('High', 'High'),('Medium', 'Medium'),('Low', 'Low')]
    s_choice = [('Open', 'Open'),('In Progress', 'In Progress'),('Closed', 'Closed')]

    incident_id = models.CharField(unique=True)
    type_of_incident = models.CharField(choices=identity_field)
    reporter_name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    # datetime=models.DateTimeField(default=timezone.now)
    datetime = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(choices=p_choice)  
    status = models.CharField(choices=s_choice)  
    
   