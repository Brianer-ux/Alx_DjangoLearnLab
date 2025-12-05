from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User

from .models import Post
from .forms import RegisterForm


# --------------------
# BLOG HOME PAGE
# --------------------
def index(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/index.html', {'posts': posts})


# --------------------
# AUTHENTICATION VIEWS
# --------------------
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    auth_logout(request)
    return render(request, 'logout.html')


@login_required
def profile(request):
    user = request.user

    if request.method == 'POST':
        new_email = request.POST.get('email')
        user.email = new_email
        user.save()

    return render(request, 'profile.html', {'user': user})
