from django.contrib import admin
from .models import Habit
from .models import Day

admin.site.register(Habit)
admin.site.register(Day)