from django.db import models
from django.utils import timezone

class Habit(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.title
