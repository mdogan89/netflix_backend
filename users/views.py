from django.shortcuts import render, redirect
from .form import *
from .models import *

# Create your views here.

from django.contrib.auth import login, logout, authenticate

def register(request):
    form = UserForm
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

    context = {
        "form":form
    }
    return render(request,"register.html",context)

def userLogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        userpass = request.POST["password"]

        user = authenticate(request,username=username,password=userpass)
        if user is not None:
            login(request,user)
            return redirect("profiles")
        else:
            return render(request,"login.html")
    return render(request,"login.html")

def profiles(request):
    users = Profiles.objects.filter(owner=request.user)
    context = {
        "users": users
    }

    return render(request,"browse.html",context)

def createProfile(request):
    form = ProfileForm()
    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.owner = request.user
            profile.save()

            return redirect("profiles")
    context = {
        "form": form
    }

    return render(request,"create-profile.html",context)


def logoff(request):
    logout(request)
    return redirect("index")

def profile(request):
    profile = request.user
    context = {
        "profile" : profile
    }
    return render(request,"hesap.html",context)

def deleteUser(request):
    profile = request.user
    profile.delete()
    return redirect("index")