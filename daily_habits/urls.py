from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.habits_list, name='habits_list'),
    url(r'^home/$', views.home, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^streaks/$', views.streaks, name='streaks'),
]