from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.basic),
    url(r'^new/', views.new_sse),
]
