from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


def user_login(req):
    if req.method == "POST":
        form = LoginForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(req, username=data["username"], password=data["password"])
        if user is not None:
            if user.is_active:
                login(req,user)
                return HttpResponse("Auth success")
            else:
                return HttpResponse("Disabled account")
        else:
            return HttpResponse("Invalid login")
    else:
        form = LoginForm()
    return render(req, "account/login.html", {"form":form})

@login_required
def dashboard(req):
    return render(req, "account/dashboard.html", {"section":"dashboard"})