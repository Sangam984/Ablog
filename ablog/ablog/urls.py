
from django.contrib import admin
from django.urls import path,include
from members.views import PasswordsChangeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myblog.urls')),
    path('members/',include('django.contrib.auth.urls')),
    path('members/',include('members.urls')),
    path('<int:pk>/password/',PasswordsChangeView.as_view()),

    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
