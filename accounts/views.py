from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import RegisterForm


def register_page(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have registered new account, please Login!")
            return redirect("/login")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})
