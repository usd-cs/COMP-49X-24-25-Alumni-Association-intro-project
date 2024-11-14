from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.template.loader import render_to_string
from django.http import JsonResponse

'''This function is called when someone goes to the /register URL
The function will render the register page and then actually register the user if they fill out the form.'''
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if username and email and password:
            if not User.objects.filter(email=email).exists():
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('user_login')
    return render(request, 'register.html')

'''This function is called when someone goes to the /login URL
This function will render the login page and then log a user in if they enter valid credentials, otherwise it
will display an error message and prompt the user to log in again.'''
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'login.html')
    return render(request, 'login.html')

'''This function is called when someone is on the home page looking to see the post list.
It will render the post_list.html page and provide the page with a list of all the posts.''' 
def post_list(request):
    posts = Post.objects.all().order_by('-time_posted')
    return render(request, 'post_list.html', {  # Remove 'posts/' prefix
        'posts': posts,
        'view_type': 'list'
    })

'''This function is called whenever someone clickes on a specific post.
It will render the post_detail.html page and provide all of the details on the post and comments underneath it.'''
def post_detail(request, post_id):
    post = get_object_or_404(Post, post_ID=post_id)
    comments = post.comment_set.all().order_by('-time_posted')
    comment_form = CommentForm()
    return render(request, 'post_detail.html', {  # Remove 'posts/' prefix
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'view_type': 'detail'
    })

'''This function is called whenever someone creates a post. It will render a create_post.html page and then add the post to the database.
'''
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {  # Remove 'posts/' prefix
        'form': form,
        'view_type': 'create'
    })

'''This function is called whenever someone posts a comment. It will add the comment to the database.
'''
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, post_ID=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.parent_post = post
            comment.author = request.user
            comment.save()
    return redirect('post_detail', post_id=post_id)

'''This function is called whenever an admin deletes a comment.'''
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, comment_ID=comment_id)
    if request.user.is_staff or comment.author == request.user:
        post_id = comment.parent_post.post_ID
        comment.delete()
        return redirect('post_detail', post_id=post_id)
    return redirect('home')

'''This function is called whenever an admin deletes a post.'''
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, post_ID=post_id)
    if request.user.is_staff:  # Only staff/admin can delete
        post.delete()
        return redirect('home')
    return redirect('post_detail', post_id=post_id)

'''This function is caled whenever someone logs out of the system, it will log them out and then redirect to the login page.'''
def user_logout(request):
    logout(request)
    return redirect('user_login')
