
from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.

class Details(models.Model):
   img = models.ImageField(upload_to='pics')
   pid = models.IntegerField(primary_key=True)
   first_name = models.CharField(max_length=20)
   last_name = models.CharField(max_length=20)
   building = models.CharField(max_length=20)
   weight = models.FloatField()
   gender = models.CharField(max_length=20)
   rtpcr = models.BooleanField()
   admission = models.DateField()
   remarks = models.TextField()





