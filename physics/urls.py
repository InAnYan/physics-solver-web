from django.urls import path

from physics import views

urlpatterns = [
    path('', views.index),
    path('solution', views.solution),
    path('thanks-feedback', views.thanks_feedback),
    path('thanks-report', views.thanks_report),
    path('no-link', views.no_link)
]
