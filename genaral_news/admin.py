from django.http import HttpRequest
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.html import format_html
from typing import Any
from django.contrib import admin
from .models import News, Features, SocialJournalism, Sports, PhotoStory, TheTruth
from .forms import NewsAdminForm, FeaturesAdminForm, PhotoStoryAdminForm, SocialJournalismAdminForm, SportsAdminForm, TheTruthAdminForm, imageUploadingCloudFlare


# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('content', 'heading', 'date', 'image')

class FeaturesAdmin(admin.ModelAdmin):
    form = FeaturesAdminForm
    list_display = ('content', 'heading', 'date', 'image')

class SocialJournalismAdmin(admin.ModelAdmin):
    form = SocialJournalismAdminForm
    list_display = ('content', 'heading', 'date', 'image')

class SportsAdmin(admin.ModelAdmin):
    form = SportsAdminForm
    list_display = ('content', 'heading', 'date', 'image')

class PhotoStoryAdmin(admin.ModelAdmin):
    form = PhotoStoryAdminForm
    list_display = ('content', 'heading', 'date', 'image')

class TheTruthAdmin(admin.ModelAdmin):
    form = TheTruthAdminForm
    list_display = ('content', 'heading', 'date', 'image')


admin.site.register(News, NewsAdmin)
admin.site.register(Features, FeaturesAdmin)
admin.site.register(SocialJournalism, SocialJournalismAdmin)
admin.site.register(Sports, SportsAdmin)
admin.site.register(PhotoStory, PhotoStoryAdmin)
admin.site.register(TheTruth, TheTruthAdmin)