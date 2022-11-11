from unittest.util import _MAX_LENGTH
from django.db import models

class Details(models.Model):
    name=models.CharField(max_length=1024)
    Age=models.IntegerField()

class Form(models.Model):
    First_name=models.CharField(max_length=500)
    Last_name=models.CharField(max_length=100)



# Create your models here.
# Register your app in setting installed app
# Register your models in admin.py
# mMakemigration
# Then migrate

