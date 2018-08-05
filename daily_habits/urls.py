from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.habits_list, name='habits_list'),
    url(r'^home/$', views.home, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
]