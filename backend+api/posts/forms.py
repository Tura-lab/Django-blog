from django.contrib.auth import get_user_model
from django import forms
from .models import Post, Answer, Comment

class PostCreateForm(forms.ModelForm): 
    text = forms.CharField(label='', widget=forms.Textarea())
 
    class Meta:
        fields = ('text',)
        model = Post

class AnswerForm(forms.ModelForm):
    
    class Meta:
        initial=''
        fields = ('text',)
        model = Answer


class CommentForm(forms.ModelForm):
    
    class Meta:
        fields = ('text',)
        model = Comment    