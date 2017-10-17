# coding=utf-8

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^change-my-account-data/$', views.update_user, name='update_user'),
    url(r'^change-password/$', views.update_password, name='update_password'),
    url(r'^register/$', views.register, name='register'),
]
