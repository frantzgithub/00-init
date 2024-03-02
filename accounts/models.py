from django.db import models

# Create your models here.

class Account(models.Model):
    name = models.CharField(max_length=10)
    passport = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    birthdate = models.DateField(null=True)
    is_married = models.BooleanField(default=False)
