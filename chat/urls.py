from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

from . import views

app_name = "chat"
urlpatterns = [
    path("", views.index, name="index"),
]