# google_login/urls.py
from django.urls import path, include
from .views import view_name, login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # path('accounts/google/login', login, name="custom_login"),

    path('logout', LogoutView.as_view(), name='logout'),
    path('', view_name, name="view_name"),
]
