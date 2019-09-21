from django.urls import path
from blog import views


urlpatterns = [
    path('', views.home,name='blog-home'),
    path('about/', views.about,name='blog-about'),

]
