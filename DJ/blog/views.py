from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post , Comment
from django.urls import reverse_lazy

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 5

# class CommentListView(ListView):
#     model = Comment
#     fields = ['User,timestamp,content']
#     template_name = 'blog/comment_list.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'Comments'
#     ordering = ['-date']

#     def form_valid(self, form):
#         return super().form_valid(form)

#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return Comment.objects.filter(author=user).order_by('-date')


class CommentListView(ListView):
    model = Comment
    context_object_name = 'comments'
    template_name='blog/comment_list.html'


# class CommentCreateView(CreateView):
#     model = Comment


#     def form_valid(self, form):
#         form.instance.owner = self.request.user
#         return super(CommentCreateView, self).form_valid(form)

class CommentCreateView(CreateView):
    model = Comment 
    fields = ('content',)
    template_name='blog/comment_create.html'
    def post_valid(self, form):
        post = get_object_or_404(Post, 
                                    slug=Post.slug) # Replaced 'Post' with 'Article'
        Postcomment = form.save(commit=False)
        Postcomment.author = self.request.user
        Postcomment.post = post
        Postcomment.save()
        return redirect('articles:article-detail', slug=article.slug)

    def get_success_url(self):
        blog = Post.objects.get(pk=self.kwargs.get('pk'))
        Comment = Comment.objects.get(pk1=self.kwargs.get('pk1'))
        return Comment.get_absolute_url()


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date')


class CommentDetailView(DetailView):
    model = Comment


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})