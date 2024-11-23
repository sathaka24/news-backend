from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Features, SocialJournalism, PhotoStory, Sports


# Create your views here.

def index(request):
    #calling database abtrating api to get data from database
    news = News.objects.all()
    #SELECT * FROM genaral_news_news 
    
    return HttpResponse(news.count())

def previewGenarator(request):

    urlParameter = str(request.GET.get('id', ''))
    category = urlParameter.split('-')[0]
    row_id = int(urlParameter.split('-')[1])

    match category:
        case "genaral_news":
            data = News.objects.filter(id__exact=row_id)

            context = {
                'heading': list(data.values('heading'))[0]['heading'],
                'image': list(data.values('image'))[0]['image']
            }

            return render(request, 'genaral_news/preview.html', context)
        
        case "features":
            data = Features.objects.filter(id__exact=row_id)

            context = {
                'heading': list(data.values('heading'))[0]['heading'],
                'image': list(data.values('image'))[0]['image']
            }

            return render(request, 'genaral_news/preview.html', context)
        
        case "social_journalism":
            data = SocialJournalism.objects.filter(id__exact=row_id)

            context = {
                'heading': list(data.values('heading'))[0]['heading'],
                'image': list(data.values('image'))[0]['image']
            }

            return render(request, 'genaral_news/preview.html', context)
        
        case "photo_story":
            data = PhotoStory.objects.filter(id__exact=row_id)

            context = {
                'heading': list(data.values('heading'))[0]['heading'],
                'image': list(data.values('image'))[0]['image']
            }

            return render(request, 'genaral_news/preview.html', context)
        
        case "sports":
            data = Sports.objects.filter(id__exact=row_id)

            context = {
                'heading': list(data.values('heading'))[0]['heading'],
                'image': list(data.values('image'))[0]['image']
            }

            return render(request, 'genaral_news/preview.html', context)
