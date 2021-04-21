from django.urls import path, include
from .views import PostListView, PostDetailView, PostCreateView, UpVoteView, DownVoteView, CommentView, AnswerView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('up/<int:pk>', UpVoteView, name='up-page'),
    path('down/<int:pk>', DownVoteView, name='down-page'),
    path('comment/<int:pk>', CommentView, name='comment-page'),
    path('answer/<int:pk>', AnswerView, name='answer-page'),
    path('create/', PostCreateView.as_view(), name='post-create'),
]
