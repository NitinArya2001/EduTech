from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *


@login_required
def student_home(request):
    # Logic for student home page
    return render(request, 'student_home.html')

@login_required
def student_profile(request):
    username = request.user.username
    email = request.user.email
    context = {'username': username, 'email': email}
    return render(request, 'profile.html', context)

@login_required
def student_profile_update(request):
    print("Inside student_profile_update view")
    form = StudentProfileForm(instance=request.user)
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/student_profile')

    context = {'form': form}
    return render(request, 'student_profile_form.html', context)
