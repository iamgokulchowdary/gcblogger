from django import forms
from .models import *
from .models import CustomUser as User

class SignInForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'id': 'signinEmail',
        'name': 'signinEmail',
        'required': True
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'id': 'signinPassword',
        'name': 'signinPassword',
        'required': True
    }))

class SignUpForm(forms.Form):
    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'id': 'signupName',
        'name': 'signupName',
        'required': True
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'id': 'signupEmail',
        'name': 'signupEmail',
        'required': True
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'id': 'signupPassword',
        'name': 'signupPassword',
        'required': True
    }))

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already registered.")
        return email

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

