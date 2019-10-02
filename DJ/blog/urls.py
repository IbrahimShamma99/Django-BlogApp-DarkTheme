from django.urls import path
from blog import views
from .views import ( 
    PostListView , 
    PostDetailView ,
    PostCreateView ,
    PostUpdateView,
    PostDeleteView)

urlpatterns = [
    path('', PostListView.as_view(),name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'),#http://127.0.0.1:8000/blog/post/1/
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name='post-delete'),
    path('post/new/', PostCreateView.as_view(),name='post-create'),
    path('about/', views.about,name='blog-about'),
    
]
