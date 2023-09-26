from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm,UserEditForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from .forms import PassForm

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserProfileEdit(generic.UpdateView):
    form_class = UserEditForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PassForm
    success_url = reverse_lazy('home')
    template_name = 'registration/passwords.html'




