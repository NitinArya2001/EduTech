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
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, instance=request.user.student_profile)
        if form.is_valid():
            form.save()

            # Redirect to the profile details page
            return redirect('/student_profile')
    else:
        form = StudentProfileForm()

    return render(request, 'student_profile_form.html', {'form': form})
