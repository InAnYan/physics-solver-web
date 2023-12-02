from django.urls import path

from physics import views

urlpatterns = [
    path('', views.index),
    path('solution', views.solution)
]