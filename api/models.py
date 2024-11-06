from django.db import models
from tastypie.resources import ModelResource, Resource
from tastypie.exceptions import BadRequest
from tastypie.fields import CharField, DateField, IntegerField
from genaral_news.models import News, Sports, SocialJournalism, Features, PhotoStory
# Create your models here.

#filetring algorithem
def filtering_algo(request, model):

    ids = request.GET.get('ids', None)
    page = request.GET.get('page', None)

    if not page :
        raise BadRequest("Invalid Id!")

    elif page == 'pageM':

        #protecting from bad requests
        try:
            id = int(ids)
        except:
            raise BadRequest("Invalid Id!")
        if id > 500:
            raise BadRequest("Invalid Id!")
        
        news_per_page = 15
        all_data = model.objects.all()
        total_row = all_data.count() #get currently available total records
        latest_raw = model.objects.latest('id') #get the latest row id. if some row(s) deleted then (lates row id) > (total rows)
        latest_raw_id = latest_raw.id 
        id_list = []
        
        if total_row > 15:
            starting_id = latest_raw_id - news_per_page*(id-1)
            count = 0

            while count < 15:
                if model.objects.filter(id=starting_id).exists():
                    id_list.append(starting_id)
                    count +=1

                starting_id -= 1
        else:
            for i in range(total_row):
                id_list.append(latest_raw_id)
                latest_raw_id -= 1
        
        return id_list
    
    elif page == 'pageS':


        try:
            id = int(ids)
        except:
            raise BadRequest("Invalid Id!")
        if id > 500:
            raise BadRequest("Invalid Id!")
        
        id_list = []
        id_list.append(id)
        return id_list

    
#----------------News--------------------------------------
class NewsResource(ModelResource):
    class Meta:
        queryset = News.objects.all()
        resource_name = "genaral_news"


    #under this filter data
    def apply_filters(self, request, applicable_filters):

        id_list = filtering_algo(request, News)
        applicable_filters['id__in'] = id_list

        #here we set the sending queryset to reverse order to get latest news to top
        return super().apply_filters(request, applicable_filters).order_by('-id')

    
#----------------------------Sports------------------------------------
class SportsResource(ModelResource):
    class Meta:
        queryset = Sports.objects.all()
        resource_name = "sports"
    
    #under this filter data
    def apply_filters(self, request, applicable_filters):

        id_list = filtering_algo(request, Sports)
        applicable_filters['id__in'] = id_list

        return super().apply_filters(request, applicable_filters).order_by('-id')

#---------------------Social-Journalism----------------------------------
class SocialJournalismResource(ModelResource):
    class Meta:
        queryset = SocialJournalism.objects.all()
        resource_name = "social_journalism"
    
    #under this filter data
    def apply_filters(self, request, applicable_filters):

        id_list = filtering_algo(request, SocialJournalism)
        applicable_filters['id__in'] = id_list

        return super().apply_filters(request, applicable_filters).order_by('-id')
    

#-------------------------Features--------------------------------
class FeaturesResource(ModelResource):
    class Meta:
        queryset = Features.objects.all()
        resource_name = "features"
    
    #under this filter data
    def apply_filters(self, request, applicable_filters):

        id_list = filtering_algo(request, Features)
        applicable_filters['id__in'] = id_list

        return super().apply_filters(request, applicable_filters).order_by('-id')


#-------------------------Photo-Story-----------------------------
class PhotoStoryResource(ModelResource):
    class Meta:
        queryset = PhotoStory.objects.all()
        resource_name = "photo_story"
    
    #under this filter data
    def apply_filters(self, request, applicable_filters):

        id_list = filtering_algo(request, PhotoStory)
        applicable_filters['id__in'] = id_list

        return super().apply_filters(request, applicable_filters).order_by('-id')


#---------getting-latest-two-news-from-each-category----------------------

#defininf an object. we use this class to create objects and store them in a list and will return it as returned data
    #also we will tell the tastypie to treat this class as base class to create instance.
class DataObject:

    def __init__(self, pk, heading, date, image, category):
        self.pk = pk #pk stands for primery key
        self.heading = heading
        self.date = date
        self.image = image
        self.category = category

# Here we return the latest two news from each table
class LatestTwoResource(Resource):

    # her define the response fields
    id = IntegerField(attribute="pk")
    heading = CharField(attribute="heading")
    date = DateField(attribute="date")
    image = CharField(attribute="image")
    category = CharField(attribute="category")

    class Meta:
        resource_name = 'latest'
    
    def get_object_list(self, request):
        
        news_data = News.objects.order_by('-id')[:2]
        sports_data = Sports.objects.order_by('-id')[:2]
        socialj_data = SocialJournalism.objects.order_by('-id')[:2]
        features_data = Features.objects.order_by('-id')[:2]
        photostory_data = PhotoStory.objects.order_by('-id')[:2]

        combined_data = []

        for object in news_data:
            combined_data.append(
                DataObject(object.id, object.heading, object.date, object.image, "genaral_news") #<----------------
            )

        for object in sports_data:
            combined_data.append(
                DataObject(object.id, object.heading, object.date, object.image, "sports") #<----------------
            )
        for object in socialj_data:
            combined_data.append(
                DataObject(object.id, object.heading, object.date, object.image, "social_journalism") #<----------------
            )
        for object in features_data:
            combined_data.append(
                DataObject(object.id, object.heading, object.date, object.image, "features") #<----------------
            )
        for object in photostory_data:
            combined_data.append(
                DataObject(object.id, object.heading, object.date, object.image, "photo_story") #<----------------
            )
        return combined_data
    
    def obj_get_list(self, bundle, **kwargs):
        return self.get_object_list(bundle.request)