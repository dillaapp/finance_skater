from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UserRegisterForm

# Create your views here.
from django.urls import reverse


def user_login(request):
    return render(request, 'authentication/login.html')


def user_logout(request):
    return render(request, 'authentication/logout.html')


def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('fin_skater_profile:index')
        )


def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            messages.success(request, f'Account created for {first_name}! You can now login.')
            return redirect('user_auth:login')
    else:
        form = UserRegisterForm()
    return render(request, 'authentication/register.html', {'form': form})
