from django.shortcuts import render
from django.http import HttpResponse
from datetime import timedelta

date = timedelta(microseconds=-1)

posts = [
{
	'author':'Ibrahim',
	'title':'first post',
	'content':'hello there I am using django',
	'date_posted':"22nd feb 2019"
},
{
	'author':'Judy',
	'title':'second post',
	'content':'hello there I am using django',
	'date_posted':'20th sep 2019'
}
]

Authors = [
{'Name':'Ibrahim'},
{'Name':'Judy'}
]


def home(request):
	context = {
	'posts':posts
	}
	return render(request,'blog/home.html',context)

#Create your views here.
#What user gonna see 


def about(request):
	context = {'Auths':Authors}
	return render(request,'blog/about.html',context)	
