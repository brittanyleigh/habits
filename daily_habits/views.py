from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import date, timedelta
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Day, UserInfo
from .forms import DayForm, ProfileForm

@login_required
def habits_list(request):
    today = date.today()
    habits, created = Day.objects.get_or_create(date__date=today, user=request.user)
    yesterday = today - timedelta(1)
    yesterday_habits = Day.objects.filter(date__date=yesterday, user=request.user).first()
    profile = UserInfo.objects.filter(user=request.user).first()

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
    return render(request, 'daily_habits/habits_list.html', {'habits': habits, 'form': form, 'profile': profile})

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
    return render(request, 'daily_habits/profile.html', {'form': form, 'profile': profile_settings})

@login_required
def streaks(request):
    today = date.today()
    today_habits = Day.objects.filter(date__date=today, user=request.user).first()
    yesterday = today - timedelta(1)
    yesterday_habits = Day.objects.filter(date__date=yesterday, user=request.user).first()
    profile = UserInfo.objects.filter(user=request.user).first()

    habitOneStreakStart = Day.objects.filter(date__lte=yesterday, habitOneCompleted=False, user=request.user).order_by('-date').first()
    habitOneStreak = (today - habitOneStreakStart.date.date()).days 
    if not yesterday_habits.habitOneCompleted:
        habitOneStreak = 0
    if today_habits and today_habits.habitOneCompleted:
        habitOneStreak += 1

    habitTwoStreakStart = Day.objects.filter(date__lte=yesterday, habitTwoCompleted=False, user=request.user).order_by('-date').first()
    habitTwoStreak = (today - habitTwoStreakStart.date.date()).days 
    if not yesterday_habits.habitTwoCompleted:
        habitTwoStreak = 0
    if today_habits and today_habits.habitTwoCompleted:
        habitTwoStreak += 1

    habitThreeStreakStart = Day.objects.filter(date__lte=yesterday, habitThreeCompleted=False, user=request.user).order_by('-date').first()
    habitThreeStreak = (today - habitThreeStreakStart.date.date()).days 
    if not yesterday_habits.habitThreeCompleted:
        habitThreeStreak = 0
    if today_habits and today_habits.habitThreeCompleted:
        habitThreeStreak += 1

    return render(request, 'daily_habits/streaks.html', {'habitOne': habitOneStreak, 'habitTwo': habitTwoStreak, 'habitThree': habitThreeStreak, 'profile': profile})


