from django.db import models
from django import forms

# Create your models here.
class LoginForm(models.Model):
    # Define your model fields here
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()

    def __str__(self):
        return self.field1