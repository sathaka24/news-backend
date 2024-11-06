from django.db import models

# Create your models here.

class News(models.Model):
    content = models.TextField()
    heading = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField() #<---------
    image = models.CharField(max_length=255, null=True, blank=True)

class Features(models.Model):
    content = models.TextField()
    heading = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField() #<---------
    image = models.CharField(max_length=255, null=True, blank=True)

class SocialJournalism(models.Model):
    content = models.TextField()
    heading = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField() #<---------
    image = models.CharField(max_length=255, null=True, blank=True)

class PhotoStory(models.Model):
    content = models.TextField()
    heading = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField() #<---------
    image = models.CharField(max_length=255, null=True, blank=True)

class Sports(models.Model):
    content = models.TextField()
    heading = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField() #<---------
    image = models.CharField(max_length=255, null=True, blank=True)