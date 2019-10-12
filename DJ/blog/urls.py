from django.urls import path , include
from blog import views
from .views import ( 
    PostListView , 
    PostDetailView ,
    PostCreateView ,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    CommentCreateView,
    CommentListView,
    CommentDetailView)

urlpatterns = [
    path('', PostListView.as_view(),name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'),#http://127.0.0.1:8000/blog/post/1/
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name='post-delete'),
    path('post/new/', PostCreateView.as_view(),name='post-create'),
    path('about/', views.about,name='blog-about'),
    
    path('post/<int:pk>/comment/new', CommentCreateView.as_view(),name='comments-create'),
    path('post/<int:pk>/comments/', CommentListView.as_view(),name='blog-comments'),
    path('post/<int:pk>/comment/<int:pkc>/', CommentDetailView.as_view(),name='comment-detail'),


]
