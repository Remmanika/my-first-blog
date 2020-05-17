from django.urls import path
from . import views

urlpatterns = [
	patg('', views.post_list, name='post_list'),
]