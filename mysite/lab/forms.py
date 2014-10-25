# -*- coding: utf-8 -*-
from models import Professor
from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ProfessorProfileForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ('born', 'identification_card', 'department')

