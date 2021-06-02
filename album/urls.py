from django.urls import include, path
from django.urls.resolvers import URLPattern

from . import views

app_name = 'album'

urlpatterns = [
    path('', views.album, name='album')
]
