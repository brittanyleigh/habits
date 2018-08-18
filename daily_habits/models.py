from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser

class Day(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    habitOneCompleted = models.BooleanField(default=False)
    habitTwoCompleted = models.BooleanField(default=False)
    habitThreeCompleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.date.date())

class UserInfo(models.Model): 
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    habitOne = models.CharField(max_length=20, default='Eat Well')
    habitTwo = models.CharField(max_length=20, default='Meditate')
    habitThree = models.CharField(max_length=20, default='Exercise')

    def __str__(self):
        return self.user.username
