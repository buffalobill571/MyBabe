from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.basic),
    url(r'^sub/', views.xss),
]
