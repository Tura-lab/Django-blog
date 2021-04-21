from rest_framework import serializers
from posts.models import Post, Answer, Comment
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'is_active', 'is_staff')

class CommentListSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    answer = serializers.PrimaryKeyRelatedField(queryset=Answer.objects.all()) 
    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'answer', 'date_posted', 'date_edited', 'show_identity')

class AnswerListSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())  
    comments = CommentListSerializer(many=True, read_only=True)
    votes = serializers.IntegerField(read_only=True) 
    
    class Meta:
        model = Answer
        fields = ('id', 'text', 'post', 'author', 'comments', 'date_posted', 'date_edited', 'show_identity', 'comment_count', 'votes')
        depth = 1

class PostListSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    answers = AnswerListSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'answers', 'date_posted', 'date_edited', 'show_identity', 'answer_count')
        depth = 1

