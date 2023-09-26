from django import forms
from .models import Post,Category,Profile
choices = Category.objects.all().values_list('name','name')
choices_list = []
for item in choices:
    choices_list.append(item)
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','category','body','image_upload')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            # 'author':forms.Select(attrs={'class':'form-control'}),
            'author' : forms.TextInput(attrs={'class':'form-control','id':'elder','type':'hidden','value':''}),
            'category':forms.Select(choices=choices_list,attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','body')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your title Here'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','website_url','facebook_url','insta_url','twitter_url')
        widgets = {
            # 'user':forms.TextInput(attrs={'class':'form-control','id':'sangam','type':'hidden','value':''}),
            'bio':forms.TextInput(attrs={'class':'form-control'}),
            'website_url':forms.TextInput(attrs={'class':'form-control'}),
            'facebook_url':forms.TextInput(attrs={'class':'form-control'}),
            'insta_url':forms.TextInput(attrs={'class':'form-control'}),
            'twitter_url':forms.TextInput(attrs={'class':'form-control'}),
        }

