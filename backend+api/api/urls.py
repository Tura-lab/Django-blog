from django.urls import path
from .views import (
    QuestionListView,
    QuestionDetailView, 
    AnswerDetailView, 
    AnswerCreateView, 
    CommentCreateView, 
    CommentDetailView,
    QuestionCreateView
)

urlpatterns = [
    path('posts/', QuestionListView.as_view(),name='api-list'),
    path('post/create/', QuestionCreateView.as_view()),
    path('post/<int:pk>/', QuestionDetailView.as_view(), name='api-detail'),
    path('answer/create/', AnswerCreateView.as_view()),
    path('answer/<int:pk>/', AnswerDetailView.as_view()),
    path('comment/create/', CommentCreateView.as_view()),
    path('comment/<int:pk>/', CommentDetailView.as_view()),
]