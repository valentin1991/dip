from django.urls import path
from . import views


# data = {'link': ListLink.objects.all()}

urlpatterns = [
    path('', views.home, name = 'cut-home'),
    path('shortlink/',views.CreateShortLink.as_view(), name = 'createlink'),

]
