from django.db import models

# Create your models here.

# Model for Bank Table

class Bank(models.Model):
    name = models.CharField(max_length=49, blank=True, null=True, unique=True)
    id = models.BigIntegerField(primary_key=True,default=000000)

 # Model for Bank Table

class Branch(models.Model):
    ifsc = models.CharField(primary_key=True, max_length=11)
    bank_id = models.ForeignKey(Bank, models.DO_NOTHING)
    branch = models.CharField(max_length=74 )
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)

    