
from django.urls import path
from .views import UserRegisterView,UserProfileEdit,PasswordsChangeView
urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
    path('edit-Profle/',UserProfileEdit.as_view(),name='profile_edit'),
    # path('password/',PasswordsChangeView.as_view()),
    
    
    
]
