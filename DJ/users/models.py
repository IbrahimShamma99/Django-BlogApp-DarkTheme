from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default ='default.jpeg',upload_to='profile_pics')
#upload_to is the image dir when uploaded to a file
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img = Image.open(self.image.path)
        limit = 300
        if img.height > limit or img.width > limit :
            size = (limit , limit )
            img.thumbnail(size ,  Image.ANTIALIAS) 
            img.save(self.image.path)