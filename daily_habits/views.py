from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import date
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Day, UserInfo
from .forms import DayForm, ProfileForm

@login_required
def habits_list(request):
    today = date.today()
    habits, created = Day.objects.get_or_create(date__date=today, user=request.user)
    profile_settings = UserInfo.objects.filter(user=request.user).first()

    if request.method == "POST":
        form = DayForm(request.POST, instance=habits)
        if form.is_valid():
            day = form.save(commit=False)
            day.user = request.user
            day.date = timezone.now()
            day.save()
            return redirect('/')
    else:
        form = DayForm()
    return render(request, 'daily_habits/habits_list.html', {'habits': habits, 'form': form, 'profile': profile_settings})

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

@login_required
def profile(request):
    profile_settings = UserInfo.objects.filter(user=request.user).first()

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile_settings)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('/')
    else:
        form = ProfileForm()
    return render(request, 'daily_habits/profile.html', {'form': form})

@login_required
def streaks(request):
    habits = Day.objects.filter(user=request.user).order_by('-date')

    for x in habits:
      if x.eatHealthyCompleted:
        streaks.eat_streak += 1
      else:
        break

    return render(request, 'daily_habits/streaks.html', {'streaks': streaks})
