from django.urls import path
from .views import schedule_index, schedule_get

urlpatterns = [
    path('get', schedule_get, name="schedule_get"),
    path('', schedule_index, name="schedule_index"),
]