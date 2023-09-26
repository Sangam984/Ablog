from typing import Any
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First name'}))
    last_name = forms.CharField( max_length=200,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last nam'}))



    class meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        # ordering = ('username','first_name','last_name','email','password1','password2')

        
    def __init__(self, *args, **kwargs) -> None:
        super(SignUpForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'
    
class UserEditForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length = 200,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    is_staff = forms.ChoiceField(widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_active = forms.ChoiceField(widget=forms.CheckboxInput(attrs={'class':'form-check'}))


    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','is_staff','is_active']

class PassForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Old password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter New Password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Retype The Password'}))

    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']