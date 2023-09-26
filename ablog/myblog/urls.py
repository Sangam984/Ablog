
from django.urls import path
from .views import HomeView,ArticleView,AddPostView,UpdatePostView,DeletePostView,AddCategoryView,CategoryView,likeView,CreateProfile
urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('article/<int:pk>',ArticleView.as_view(),name = 'article-view'),
    path('addPost/',AddPostView.as_view(),name="add-post"),
    path('article/update/<int:pk>',UpdatePostView.as_view(),name='update'),
    path('article/<int:pk>/remove',DeletePostView.as_view(),name="delete"),
    path('AddCategory/',AddCategoryView.as_view(),name = 'add-category'),
    path('category/<str:cats>/',CategoryView,name = 'category'),
    path('like/<int:pk>',likeView,name='like-post'),
    path('profile/<int:pk>',CreateProfile.as_view(),name='prof')
    
]
