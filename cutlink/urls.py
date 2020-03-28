
from django.contrib import admin
from django.urls import path
from users import views as userViews
from django.urls import include, path
from django.contrib.auth import views as authViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cut.urls')),
    path('reg/', userViews.register, name = 'reg'),
    path('user/', authViews.LoginView.as_view(template_name = 'users/user.html') , name = 'user'),
    path('profile/', userViews.profile, name = 'profile'),
    path('exit/', authViews.LogoutView.as_view(template_name = 'users/exit.html') , name = 'exit'),


]
