from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from posts.models import Answer,Post,Comment
from .serializers import (
    PostListSerializer, 
    CommentListSerializer,
    AnswerListSerializer,
    )

from .permissions import IsAuthorOrReadonly

class QuestionListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

class QuestionCreateView(generics.CreateAPIView):
    queryset = Post
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user) 

class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post 
    serializer_class = PostListSerializer
    permission_classes = [IsAuthorOrReadonly,] 

class AnswerCreateView(generics.CreateAPIView):
    queryset = Answer
    serializer_class = AnswerListSerializer 
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        post_id = self.request.POST.get('post')
        serializer.save(post=Post.objects.get(id=post_id), author=self.request.user)

class AnswerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerListSerializer
    permission_classes = [IsAuthorOrReadonly]

class CommentCreateView(generics.CreateAPIView):
    queryset = Comment
    serializer_class = CommentListSerializer  
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        answer_id = self.request.POST.get('answer')
        serializer.save(answer=Answer.objects.get(id=answer_id), author=self.request.user) 
 
class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    permission_classes = [IsAuthorOrReadonly]