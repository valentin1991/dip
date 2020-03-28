from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class ListLink(models.Model):
    avtor = models.ForeignKey(User, on_delete = models.CASCADE)
    long_link = models.URLField(max_length=250, verbose_name = 'Длинная ссылка')
    short_link = models.CharField(max_length=100, verbose_name = 'Короткая ссылка')

    def get_absolute_url(self):
        return reverse('createlink')
