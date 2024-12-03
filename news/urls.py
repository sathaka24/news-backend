"""news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.models import NewsResource, SportsResource, FeaturesResource, SocialJournalismResource, PhotoStoryResource, TheTruthResource, LatestTwoResource

news_resource = NewsResource()
sports_resource = SportsResource()
features_resource = FeaturesResource()
social_journalism_resource = SocialJournalismResource()
photo_story_resource = PhotoStoryResource()
the_truth = TheTruthResource()
latest_two = LatestTwoResource()

urlpatterns = [
    path('bigboss/', admin.site.urls),
    path('genaral_news/', include("genaral_news.urls")),
    path('api/', include(news_resource.urls)),
    path('api/', include(sports_resource.urls)),
    path('api/', include(features_resource.urls)),
    path('api/', include(social_journalism_resource.urls)),
    path('api/', include(photo_story_resource.urls)),
    path('api/', include(the_truth.urls)),
    path('api/', include(latest_two.urls))
]
