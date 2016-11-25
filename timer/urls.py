from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.hello),
    url(r'^now/$', views.current_time),
    url(r'^ahead/(\d{1,2})$', views.hours_ahead),
    url(r'^temp/(\d{1,2})$', views.temp_ahead),
    url(r'^just$', views.just_meta),
    url(r'^good$', views.good_meta),
]
