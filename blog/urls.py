from django.urls import path
from . import views
from .models import Post

urlpatterns = [
    path('', views.post_list, name='post_list'),
]