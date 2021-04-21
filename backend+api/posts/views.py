from django import http
from .models import Post, Answer, Comment
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .forms import PostCreateForm, AnswerForm, CommentForm
from django.shortcuts import get_object_or_404

def AnswerView(request, pk):
    q_id = request.POST.get('q_id')
    q = get_object_or_404(Post, id=q_id)

    answer = Answer()
    answer.text = request.POST.get('answer-text')
    if answer.text == '':
        return http.HttpResponseRedirect(reverse('post-detail', args=[str(q_id)]))
    answer.author = request.user
    answer.post = q
    answer.save()
    
    return http.HttpResponseRedirect(reverse('post-detail', args=[str(q_id)]))

def CommentView(request, pk):
    ans_id = request.POST.get('ans_id')
    q_id = request.POST.get('q_id')

    ans = get_object_or_404(Answer, id=ans_id)
    comment = Comment()
    comment.text = request.POST.get('comment-text')
    if comment.text == '':
        return http.HttpResponseRedirect(reverse('post-detail', args=[str(q_id)]))
    comment.author = request.user
    comment.answer = ans
    comment.save()

    return http.HttpResponseRedirect(reverse('post-detail', args=[str(q_id)]))

def UpVoteView(request, pk):
    ans_id = request.POST.get('ans_id')
    q_id = request.POST.get('q_id')

    ans = get_object_or_404(Answer, id=ans_id)
    ans.votes = ans.votes + 1
    ans.save()

    return http.HttpResponseRedirect(reverse('post-detail', args=[str(q_id)]))

def DownVoteView(request, pk):
    ans_id=request.POST.get('ans_id')
    q_id = request.POST.get('q_id')

    ans = get_object_or_404(Answer, id=ans_id)
    ans.votes = ans.votes - 1
    ans.save()

    return http.HttpResponseRedirect(reverse('post-detail', args=[str(q_id)]))

class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'q_list'
    template_name = 'posts/post_list.html'

class PostDetailView(DetailView):
    context_object_name = 'q'
    queryset = Post.objects.all()
    template_name = 'posts/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostCreateForm
    model = Post
    template_name = 'posts/create_post.html'

    def form_valid(self, form, *args, **kwargs):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()        

        return http.HttpResponseRedirect(reverse('post-detail', kwargs={'pk':obj.id}))

