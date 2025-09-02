from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth import logout as bloglogout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .forms import *
from .models import *
from .models import CustomUser as User

# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    success = False

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                message=message
            )
        messages.success(request, "Your message was sent successfully!")

    return render(request, 'blog/contact.html')

def blogs(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(author__name__icontains=query)
        ).order_by('-created_at')

        print(posts)
    else:
        posts = Post.objects.order_by('-created_at')
    return render(request, 'blog/blogs.html', {'posts': posts})

def blog(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.select_related('author').order_by('-created_at')

    if request.method == 'POST':
        if request.user.is_authenticated:
            content = request.POST.get('comment')
            if content:
                Comment.objects.create(post=post, author=request.user, content=content)
                return redirect('blogapp:blog', slug=slug)
        else:
            return redirect('login')
        
    return render(request, 'blog/blog.html', {'post': post, 'comments': comments})


@login_required(login_url='blogapp:auth')
def createpost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')

        if not title or not content:
            messages.error(request, "Title and content are required.")
        else:
            post = Post.objects.create(
                title=title,
                content=content,
                image=image,
                author=request.user
            )
            messages.success(request, "Post created successfully.")
            return redirect('blogapp:blog', slug=post.slug)

    return render(request, 'blog/createpost.html')

@login_required(login_url='blogapp:auth')
def myposts(request):
    query = request.GET.get('q', '')
    user_posts = Post.objects.filter(author=request.user)

    if query:
        user_posts = user_posts.filter(
            Q(title__icontains=query)
        )

    user_posts = user_posts.order_by('-created_at')
    return render(request, 'blog/myposts.html', {
        'posts': user_posts,
        'query': query
    })

@login_required(login_url='blogapp:auth')
def editpost(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        if request.user == post.author:
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return redirect('blogapp:blog', slug=post.slug)
        else:
            messages.error(request, "You are not authorized to edit this post.")
            form = PostForm(instance=post)

    return render(request, 'blog/editpost.html', {'form': form})

@login_required(login_url='blogapp:auth')
def deletepost(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        if request.user == post.author:
            post.delete()
            messages.success(request, "Post deleted successfully.")
            return redirect("blogapp:myposts")
        else:
            messages.error(request, "You are not authorized to delete this post.")
            return redirect("blogapp:myposts")


@login_required(login_url='blogapp:auth')
def profile(request):
    user = request.user

    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.bio = request.POST.get('bio')

        if request.FILES.get('profileImage'):
            user.avatar = request.FILES['profileImage']

        user.save()
        messages.success(request, 'Profile Updated ')
        return redirect('blogapp:profile') 

    return render(request, 'blog/profile.html', {'user': user})

def auth(request):
    signup_form = SignUpForm()
    signin_form = SignInForm()
    error = None
    show_signin = False

    if request.method == 'POST':
        if 'signup' in request.POST:
            signup_form = SignUpForm(request.POST)
            if signup_form.is_valid():
                name = signup_form.cleaned_data['name']
                email = signup_form.cleaned_data['email']
                password = signup_form.cleaned_data['password']

                user = User.objects.create_user(
                    username=email,
                    email=email,
                    password=password,
                    name=name
                )
                login(request, user)
                messages.success(request, 'SignUp Successful')
                return redirect('blogapp:blogs')
            else:
                error = "Please correct the errors in the sign-up form."

        elif 'signin' in request.POST:
            signin_form = SignInForm(request.POST)
            show_signin = True
            if signin_form.is_valid():
                email = signin_form.cleaned_data['email']
                password = signin_form.cleaned_data['password']

                try:
                    username = User.objects.get(email=email).username
                    user = authenticate(request, username=username, password=password)
                except User.DoesNotExist:
                    user = None

                if user is not None:
                    login(request, user)
                    messages.success(request, 'SignIn Successful')
                    return redirect('blogapp:blogs')
                else:
                    error = "Invalid email or password."

    return render(request, 'blog/auth.html', {
        'signupform': signup_form,
        'signinform': signin_form,
        'error': error,
        'show_signin': show_signin
    })

@login_required(login_url='blogapp:auth')
def changePassword(request):
    if request.method == 'POST':
        current = request.POST.get('currentPassword')
        new = request.POST.get('newPassword')
        confirm = request.POST.get('confirmPassword')

        user = request.user

        if not user.check_password(current):
            messages.error(request, "Current password is incorrect.")
        elif new != confirm:
            messages.warning(request, "New passwords do not match.")
        else:
            user.set_password(new)
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password updated successfully.")
            return redirect('blogapp:profile')

    return render(request, 'blog/changepassword.html')

@login_required(login_url='blogapp:auth')
def logout(request):
    # bloglogout --> django built-in logout() used as bloglogout due to name clash
    bloglogout(request)
    nexturl = request.GET.get('next', 'blogapp:signin')
    messages.success(request, 'Logout Successful')
    return redirect(nexturl)

