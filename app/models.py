from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATE_CHOICES = (
    ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Asam','Asam'),
    ('Bihar','Bihar'),
    ('Chandigarh','Chandigarh'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Daman and Diu','Daman and Diu'),
)

class Customer(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField(default=0)
    state = models.CharField(choices=STATE_CHOICES,max_length=50)

    def __str__(self):
        return str(self.id)

class Project(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    project = models.CharField(max_length=200,default=None)