from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
class Post(models.Model):
    title = models.CharField(max_length=100) #CharField used for names restricted strings
    content = models.TextField() #unrestricted string there is "choices" parameter used for choose your own charfields
    date = models.DateTimeField(default=timezone.now()) 
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})