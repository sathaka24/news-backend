from django.contrib import admin
from .models import News, Features, SocialJournalism, Sports, PhotoStory
from .forms import NewsAdminForm, FeaturesAdminForm, PhotoStoryAdminForm, SocialJournalismAdminForm, SportsAdminForm

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


admin.site.register(News, NewsAdmin)
admin.site.register(Features, FeaturesAdmin)
admin.site.register(SocialJournalism, SocialJournalismAdmin)
admin.site.register(Sports, SportsAdmin)
admin.site.register(PhotoStory, PhotoStoryAdmin)