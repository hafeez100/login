from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('success/', views.success, name='success'),
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]


