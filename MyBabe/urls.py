from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^comet/', include('comet.urls')),
    url(r'^timer/', include('timer.urls')),
    url(r'^expo/(?P<var>[0-9]{4})/', include('expo.urls'), {'extra': 'point'}),
    url(r'^parabellum/', include('parabellum.urls')),
    url(r'^den/', include('den.urls')),
]
