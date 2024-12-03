from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class News(models.Model):
    content = RichTextField()
    heading = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField() #<---------
    image = models.CharField(max_length=255, null=True, blank=True)

class Features(models.Model):
    content = RichTextField()
    heading = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField() #<---------
    image = models.CharField(max_length=255, null=True, blank=True)

class SocialJournalism(models.Model):
    content = RichTextField()
    heading = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField() #<---------
    image = models.CharField(max_length=255, null=True, blank=True)

class PhotoStory(models.Model):
    content = RichTextField()
    heading = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField() #<---------
    image = models.CharField(max_length=255, null=True, blank=True)

class Sports(models.Model):
    content = RichTextField()
    heading = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField() #<---------
    image = models.CharField(max_length=255, null=True, blank=True)

class TheTruth(models.Model):
    content = RichTextField()
    heading = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField() #<---------
    image = models.CharField(max_length=255, null=True, blank=True)