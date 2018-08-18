from django import forms

from .models import Day, UserInfo

class DayForm(forms.ModelForm):

    class Meta:
        model = Day
        fields = ('habitOneCompleted', 'habitTwoCompleted', 'habitThreeCompleted')

class ProfileForm(forms.ModelForm):

    class Meta:
        model = UserInfo
        fields = ('habitOne', 'habitTwo', 'habitThree')
    