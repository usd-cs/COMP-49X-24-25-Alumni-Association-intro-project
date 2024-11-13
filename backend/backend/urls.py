"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from intro_proj.views import register, user_login, user_logout

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='home'),
    path('register', register, name='register'),
    path('login', user_login, name='login'),
    path('admin/', admin.site.urls),
    path('logout', user_logout, name='logout'),
]
