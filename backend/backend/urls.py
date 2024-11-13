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
from intro_proj.views import (
    register, 
    user_login, 
    post_list, 
    post_detail, 
    create_post, 
    add_comment, 
    delete_comment
)

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='home'),
    path('register', register, name='register'),
    path('login', user_login, name='login'),
    path('admin/', admin.site.urls),
    #Post Urls
    path('posts/', post_list, name='post_list'),
    path('posts/create/', create_post, name='create_post'),
    path('posts/<int:post_id>/', post_detail, name='post_detail'),
    path('posts/<int:post_id>/comment/', add_comment, name='add_comment'),
    path('comments/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
]
