from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(default=' ',max_length=100) #CharField used for names restricted strings
    content = models.TextField(default=' ') #unrestricted string there is "choices" parameter used for choose your own charfields
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    blog_id = Post.id
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    # Name = models.CharField(max_length=100)
    # Email = models.EmailField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    # Active = models.BooleanField(default=True)
    # Parent = models.ForeignKey("self", on_delete=models.CASCADE , null=True,blank=True,related_name="replies")
    class Meta:
        verbose_name = 'blog Comment'
        verbose_name_plural = 'blog Comments'
        
    def get_absolute_url(self):
        return reverse('comment-detail', kwargs={'pkc': self.pkc})

    def __str__(self):
        return "{},{},".format(self.content,self.author) 
