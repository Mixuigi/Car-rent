from django.conf.urls import url
from django.contrib.auth import logout
from django.urls import path, re_path
from . import views
from KursRabota.views import *

urlpatterns = [
    url(r'^login/$', views.Authentication, name='authentication'),
    url('registr/', register, name='registr'),
    url('^logout/$', views.Logout, name='logout'),
    path('', views.Home, name='Home_Page'),
    #path('KursRabota/<car_for_comment>/', views.add_comment_for_car, name='get_car_for_comment'),
    path('KursRabota/<car>/', views.UserCabinet, name='rent_car_number'),

]
