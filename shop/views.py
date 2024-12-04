from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .utils.context import context_home

def index(request):
    context = context_home()
    return render(request, "shop/index.html", context)

@login_required()
def dashboard(request):
    return render(request, "shop/dashboard/dashboard.html")





############### AUTHENTICATION ###############

def login(request):
    # This is a backup logic if the authentication checking in
    # in the template doesn't work
    if request.user.is_authenticated:
        return redirect("shop:dashboard")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                auth_login(request, user)
                messages.success(request, "Login Successful")
                return redirect("shop:dashboard")
    else:
        form = AuthenticationForm()

    c = {"form":form }    
    return render(request, "shop/auth/login.html", c)

def logout(request):
    auth_logout(request)
    messages.success(request, "You’re now logged out. Have a great day!")
    return redirect("shop:login")

def signup(request):
    if request.user.is_authenticated:
        return redirect("shop:index")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            auth_login(request, form.save())
            return redirect("shop:login")
    else:
        form = UserCreationForm()

    c = {"form":form}
    return render(request, "shop/auth/signup.html", c)