from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey(get_user_model(), related_name='posts', on_delete=models.CASCADE)
    text = models.TextField()
    show_identity = models.BooleanField(default=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

    def answer_count(self):
        return self.answers.count()

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.text
    

class Answer(models.Model):
    text = models.TextField()
    author = models.ForeignKey(get_user_model(), related_name='answers', on_delete=models.CASCADE) 
    show_identity = models.BooleanField(default=False)
    post = models.ForeignKey(Post, related_name='answers', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.text
    
    def comment_count(self):
        return self.comments.count()
    

    class Meta:
        ordering = ['-votes']
    

class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(get_user_model(), related_name='comments', on_delete=models.CASCADE)
    show_identity = models.BooleanField(default=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    answer = models.ForeignKey(Answer, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['date_posted']

    def __str__(self):
        return self.text