from django.urls import include, path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='blog_list')
]
