from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'cut-home'),
    path('shortlink/',views.CreateShortLink.as_view(), name = 'createlink'),
    path('about/', views.about, name ='about'),
]
