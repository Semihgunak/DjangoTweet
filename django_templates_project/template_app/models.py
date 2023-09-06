from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
# Create your models here.
class Musician(models.Model):
    name=models.CharField(max_length=50)
    instrument=models.CharField(max_length=50)
    age=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(150)])
    salary= models.IntegerField(default=0,validators=[MinValueValidator(0)])

class Tweet(models.Model):
    username=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    message=models.CharField(max_length=200)

    def __str__(self):
        return f"Tweet user: {self.username} message : {self.message}"