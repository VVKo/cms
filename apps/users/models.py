from django.db import models

from django.conf import settings


class Role(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField('Name', max_length=128)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.user.username} -> {self.team.name} -> {self.role.name}"