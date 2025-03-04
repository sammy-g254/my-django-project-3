from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from .models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
