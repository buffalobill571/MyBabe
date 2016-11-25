from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^search/', views.search),
    url(r'^contact/', views.contact),
]
