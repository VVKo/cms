from django.shortcuts import render

from .forms import bootstrap_login


def view_name(request):
    return render(request, 'users/home.html', {})


def login(request):
    if request.method == "POST":
        print('request.POST',request.POST)

    context = {
        'form': bootstrap_login(),
    }
    return render(request, 'users/login.html', context)
