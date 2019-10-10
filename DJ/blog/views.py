from django.shortcuts import render , get_object_or_404
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.mixins	import LoginRequiredMixin , UserPassesTestMixin
from django.views.generic import (
	ListView, 
	DetailView,
	CreateView,
 	UpdateView,
  	DeleteView)
from .forms import *

def home(request):
	context = {
	'posts':Post.objects.all()
	}
	return render(request,'blog/home.html',context)

#Create your views here.
#What user gonna see 

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 5
 
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5
    template_name = 'blog/user_post.html'

    def getqueryset(self):
        user = get_object_or_404(User ,username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-date")

class PostDetailView(DetailView):
	model = Post()

class PostCreateView(LoginRequiredMixin,CreateView):
	model =Post
	fields = ['title','content']#template_name = "create.html"
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model =Post
	fields = ['title','content']
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Post
	success_url = '/blog'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False
 
# def PostViews(request):
#     posts = Post.object.all()
#     return render(request,'blog/home.html')	


# def something(request):
#     model = Post()
#     comments = model.comments.filter(Active=True)
#     if(request.method == 'post'):
#      	comment_form = CommentForm
# 		if comment_form.is_valid():
# 			Parent_obj = None
# 			try:
# 				Parent_id = int(request.POST.get("Parent_id"))
# 			except :
# 				Parent_id = None
# 			if Parent_id :
# 				Parent_obj = Comment.object.get(id=Parent_id)


#<app>/<models><viewtype>.html
def about(request):
	return render(request,'blog/about.html')	
