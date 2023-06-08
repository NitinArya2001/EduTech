from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib import messages
from teachers.models import *
from students.models import *
from students.forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse

from .forms import *

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get('category')

            if role == 'teacher':
                teacher_group, created = Group.objects.get_or_create(name='teacher')
                user.groups.add(teacher_group)
                TeacherProfileForm.objects.create(user=user)
            elif role == 'student':
                student_group, created = Group.objects.get_or_create(name='student')
                user.groups.add(student_group)
                StudentProfileForm.objects.create(user=user)

            group = Group.objects.get(name=role)
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('login/')

    context = {'form': form}
    return render(request, 'register.html', context)



@csrf_protect
def loginPage(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.groups.filter(name='teacher').exists():
                    return redirect(reverse('teacher_home'))
                elif user.groups.filter(name='student').exists():
                    return redirect(reverse('student_home'))
            else:
                # Invalid credentials, display error message
                form.add_error(None, 'Invalid username or password.')

    context = {'form': form}
    return render(request, 'login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('/login')