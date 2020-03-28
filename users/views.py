
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UseerOurRegistration, UserUpdateForm

def register(request):
    if request.method == "POST":
            form = UseerOurRegistration(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Аккаунт {username} был успешно создан, введите имя пользователя и парольдля авторизации ')
                return redirect('user')
    else:
        form = UseerOurRegistration()

    return render(request, 'users/registration.html', {'form':form, 'title': 'Регистрация пользователя'})

@login_required
def profile(request):
    if request.method == "POST":

        update_user = UserUpdateForm(request.POST, instance = request.user)


        if update_user.is_valid():
            update_user.save()
            messages.success(request, f'Аккаунт был успешно обновлен ')

            return redirect('profile')

    else:
        update_user = UserUpdateForm(instance = request.user)

    data = {
    'update_user': update_user,
    'title': 'Ваш профиль'
    }
    return render(request, 'users/profile.html',data)
