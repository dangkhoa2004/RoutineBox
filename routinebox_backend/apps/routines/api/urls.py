from django.urls import path
from .views import TestRoutineApi

urlpatterns = [
    path('test/', TestRoutineApi.as_view()),
]