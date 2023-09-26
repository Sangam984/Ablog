from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=225)
    
    def __str__(self) -> str:
        return (self.name) 
    
    def get_absolute_url(self):
        # return reverse("article-view", args = (str(self.id)))
        return reverse('home')
class Post(models.Model):
    title = models.CharField(max_length=100)
    title_tag = models.CharField(max_length=100,default="Nepali Blogger")
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image_upload = models.ImageField(null = True,blank=True,upload_to="images/")
    # body = models.TextField()
    body = RichTextField(null=True,blank=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=225,default='Coding')
    likes = models.ManyToManyField(User,related_name='blog_post')
    snippets = models.CharField(max_length=200,default="Click Here")
    def total_like(self):
        return self.likes.count()
    def __str__(self) -> str:
        return self.title + ' | '+ str(self.author)
    
    def get_absolute_url(self):
        # return reverse("article-view", args = (str(self.id)))
        return reverse('home')
    
class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True,blank=True,upload_to='images/profile')
    website_url = models.CharField(max_length=255,null=True,blank=True)
    facebook_url = models.CharField(max_length=255,null=True,blank=True)
    insta_url = models.CharField(max_length=255,null=True,blank=True)
    twitter_url = models.CharField(max_length=255,null=True,blank=True)
    def __str__(self) -> str:
        return  str(self.user)
    
    def get_absolute_url(self):
        return reverse('home')
    
   