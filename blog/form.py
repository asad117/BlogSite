from dataclasses import field
import imp
from django.forms import ModelForm
from django import forms

from blog.models import Post, Comment

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"


class ContactForm(forms.Form):
    title = forms.CharField(max_length=100)
    user_name = forms.CharField(max_length=50, label="your name")
    message = forms.CharField(widget=forms.Textarea)
    
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels ={
            "user_name": "Your Name",
            "email": "Your Email",
            "text": "Your Comment"
        }
        # error_message = {
        #     "user_name":{
        #         "required": "Your name must not be empty",
        #         "max_length": "please enter the short name"
        #     }
        # }