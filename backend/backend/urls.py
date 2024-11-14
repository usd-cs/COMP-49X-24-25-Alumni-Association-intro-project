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
    user_logout,
    post_list, 
    post_detail, 
    create_post, 
    add_comment, 
    delete_comment,
    delete_post,
)
#path('', home_with_login, name='home'),

urlpatterns = [  
    path('login', user_login, name='user_login'),
    path('', post_list, name='home'),  # New homepage with posts
    path('register', register, name='register'),
    path('admin/', admin.site.urls),
    #Posts Urls
    path('posts/create/', create_post, name='create_post'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/<int:post_id>/comment/', add_comment, name='add_comment'),
    path('comments/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
    path('post/<int:post_id>/delete/', delete_post, name='delete_post'),
    path('logout', user_logout, name='logout'),
]

