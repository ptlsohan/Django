from django import forms
from django.contrib.auth.models import User
from .models import Post,Comment

#from basic_app.models import UserProfileInfo

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields= ('title','text','image')

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields= ('author','text')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields=('username','email','password')

class LoginForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username','password')
