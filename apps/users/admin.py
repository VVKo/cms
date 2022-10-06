from django.contrib import admin

from .models import Role, Membership, Team

# Register your models here.
admin.site.register(Role)
admin.site.register(Membership)
admin.site.register(Team)