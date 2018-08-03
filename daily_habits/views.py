from django.shortcuts import render

def habits_list(request):
    return render(request, 'daily_habits/habits_list.html', {})
