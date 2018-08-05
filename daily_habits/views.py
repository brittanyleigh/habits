from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import date
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Day

@login_required
def habits_list(request):
    today = date.today()
    habits = Day.objects.filter(date__date=today, user=request.user)
    return render(request, 'daily_habits/habits_list.html', {'habits': habits})

def home(request):
    return render(request, 'daily_habits/home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'daily_habits/signup.html', {'form': form})
