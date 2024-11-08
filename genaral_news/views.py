from django.shortcuts import render
from django.http import HttpResponse
from .models import News


# Create your views here.

def index(request):
    #calling database abtrating api to get data from database
    news = News.objects.all()
    #SELECT * FROM genaral_news_news 
    
    return HttpResponse(news.count())

