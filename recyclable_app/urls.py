from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="recyclable-home"),
    path('about/', views.about, name="recyclable-about"),
]