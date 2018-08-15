from django import forms

from .models import Day, UserInfo

class DayForm(forms.ModelForm):

    class Meta:
        model = Day
        fields = ('eatHealthyCompleted', 'meditateCompleted', 'exerciseCompleted')

class ProfileForm(forms.ModelForm):

    class Meta:
        model = UserInfo
        fields = ('eatHealthy', 'meditate', 'exercise')
    