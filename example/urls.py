# example/urls.py
from django.urls import path
from . import views

from example.views import index

app_name = 'your_app_name'

urlpatterns = [
    path('', index, name="index"),
    path("<int:ice_id>/", views.details, name="details"),
]