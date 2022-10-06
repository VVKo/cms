from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.decorators import login_required
from .forms import bootstrap_login
from django.contrib.auth.models import AnonymousUser
from .models import Membership


@login_required
def profile(request):
    user = get_user(request)
    return render(request, 'users/profile.html', {'user': user})


def view_name(request):
    user = get_user(request)
    if user is AnonymousUser:
        return render(request, 'guest.html', {})
    else:
        try:
            if '@chnu.edu.ua' in user.email or '@chnu.cv.ua' in user.email:
                roles = get_user_roles_cms(user)
                return render(request, 'users/home.html', {"user": user, "roles": roles})
        except AttributeError:
            return render(request, 'guest.html', {"user": user})
    return render(request, 'guest.html', {"user": user})


def login(request):
    if request.method == "POST":
        print('request.POST', request.POST)

    context = {
        'form': bootstrap_login(),
    }
    return render(request, 'users/login.html', context)


def get_user_roles_cms(user):

    memb = Membership.objects.filter(user=user)
    return [mem.team for mem in memb]

