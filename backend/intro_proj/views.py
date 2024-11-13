from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if username and email and password:
            if not User.objects.filter(email=email).exists():
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

#Post Views    
def post_list(request):
    posts = Post.objects.all().order_by('-time_posted')
    return render(request, 'post_list.html', {
        'posts': posts,
        'view_type': 'list'
    })

def post_detail(request, post_id):
    post = get_object_or_404(Post, post_ID=post_id)
    comments = post.comment_set.all().order_by('-time_posted')
    comment_form = CommentForm()
    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'view_type': 'detail'
    })

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {
        'form': form,
        'view_type': 'create'
    })

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

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, comment_ID=comment_id)
    if request.user.is_staff or comment.author == request.user:
        post_id = comment.parent_post.post_ID
        comment.delete()
        return redirect('post_detail', post_id=post_id)
    return redirect('post_list')
