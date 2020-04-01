from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UsernameField
from django.db import models
from django.db.models import Model
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)


class UseerOurRegistration(forms.ModelForm):
    email = forms.EmailField(required = True)


    class Meta:
        model = User
        fields = ("username", "email")
        field_classes = {'username': UsernameField}

    error_messages = {
        'password_mismatch': ('The two password fields didn’t match.'),
    }
    password1 = forms.CharField(
        label=("Пароль"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Имя"

    def _post_clean(self):
        super()._post_clean()
        password = self.cleaned_data.get('password1')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except forms.ValidationError as error:
                self.add_error('password1', error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
