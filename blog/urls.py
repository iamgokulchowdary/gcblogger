from django.urls import path
from . import views

app_name = 'blogapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),

    path('blog/<slug:slug>', views.blog, name='blog'),
    path('blogs', views.blogs, name='blogs'),

    path('myposts', views.myposts, name='myposts'),
    path('createpost', views.createpost, name='createpost'),
    path('editpost/<slug:slug>', views.editpost, name='editpost'),
    path('deletepost/<slug:slug>', views.deletepost, name='deletepost'),

    path('profile', views.profile, name='profile'),
    path('changepassword', views.changePassword, name='changepassword'),
    path('auth', views.auth, name='auth'),
    path('logout', views.logout, name='logout'),
]
