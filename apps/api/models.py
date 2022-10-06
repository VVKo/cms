from django.db import models


class API(models.Model):
    name = models.CharField(max_length=128, verbose_name='Назва API')
    api_id = models.CharField(max_length=128, verbose_name='Ідентифікатор введення в дію')

    def __str__(self):
        return f"{self.name}"
