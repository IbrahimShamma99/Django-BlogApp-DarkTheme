from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post
#from django.test.simple import DjangoTestSuiteRunner

class PostTestCase(TestCase):
    
    def setUp(self):
        user = User.objects.filter(username='ibrahim').first()
        post1=Post(author=user,title="test1",content="Testing my Django App first time")
        post2 = Post(author=user,title="test2",content="Testing my Django App second time" )
        post1.save()
        post2.save()
        
    def test_posts_are_valid(self):
        user = User.objects.filter(username='ibrahim').first()
        post1 = Post.objects.filter(title="test1").first()
        post2 = Post.objects.filter(title="test2").first()
        self.assertEqual(post1.content, "Testing my Django App first time" )
        self.assertEqual(post2.content, "Testing my Django App second time" )
        self.assertEqual(post2.author,user)

'''

class PostTestCase(TestCase):
    
    def create_post(self,user,title,content):
        post1=Post(author=user,title= title ,content=content)        # post2 = Post(author=user,title="test2",content="Testing my Django App second time" )
        post1.save()
        # post2.save()
        return post1
        
    def test_post_creation(self):
        user = User.objects.filter(username='ibrahim').first()
        content = 'Hello World it is UnitTest !'
        title = 'test1'
        post1 = create_post(author=user,content= content ,title=title)
        # post2 = Post.objects.filter(title="test2").first()
        self.assertEqual(post1.content, content )
        # self.assertEqual(post2.content, "Testing my Django App second time" )
        self.assertEqual(post1.author,user)
'''
