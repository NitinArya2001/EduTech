from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def teacher_home(request):
    # Logic for student home page
    return render(request, 'teacher_home.html')

