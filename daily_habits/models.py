from django.db import models
from django.utils import timezone

class Habit(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Day(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    eatHealthy = models.ForeignKey(Habit, related_name='eatHealthy', on_delete=models.CASCADE)
    meditate = models.ForeignKey(Habit, related_name='meditate', on_delete=models.CASCADE)
    exercise = models.ForeignKey(Habit, related_name='exercise', on_delete=models.CASCADE)
