from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm, ProfileForm

def home_view(request):
    return render(request, "blog/home.html")

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})

@login_required
def profile_view(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileForm(instance=request.user)
    return render(request, "blog/profile.html", {"form": form})