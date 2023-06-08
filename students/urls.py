from django.urls import path
from . import views

urlpatterns = [
    path('student_home/', views.student_home, name='student_home'),
    path('student_profile/', views.student_profile, name='student_profile'),
    path('student_profile_update/', views.student_profile_update, name='student_profile_update'),
    # Add other URLs specific to the student app
]
