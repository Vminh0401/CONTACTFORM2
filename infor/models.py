from django.db import models


# Create your models here.
class Infor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    select = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)

