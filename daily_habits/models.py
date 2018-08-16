from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser

class Day(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    eatHealthyCompleted = models.BooleanField(default=False)
    meditateCompleted = models.BooleanField(default=False)
    exerciseCompleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.date.date())

class UserInfo(models.Model): 
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    eatHealthy = models.CharField(max_length=56, default='Eat Well')
    meditate = models.CharField(max_length=56, default='Meditate')
    exercise = models.CharField(max_length=56, default='Exercise')

    def __str__(self):
        return self.user.username
