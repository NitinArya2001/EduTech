from django.urls import path
from . import views

urlpatterns = [
    path('teacher_home/', views.teacher_home, name='teacher_home'),
    # Add other URLs specific to the student app
]
