from typing import Any
from django import forms
import requests
from .models import News, Features, PhotoStory, SocialJournalism, Sports
from django.conf import settings

#image uploading function for cloud-flare 

def imageUploadingCloudFlare(self, instance):
    if self.cleaned_data.get('image_upload'): #Checks if an image has been uploaded

            file = self.cleaned_data['image_upload'] #Get the upload file(image)

            account_id = settings.CLOUD_FLARE_ACC_ID

            api_token = settings.CLOUD_FLARE_API_TOKEN

            headers = {
                "Authorization": f"Bearer {api_token}"
            }

            url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1"

            response = requests.post(url=url, headers=headers, files={'file': file})

            print(response.status_code)
            print(response.content)

            if response.status_code == 200:
                access_url =  response.json()['result']['variants'][0]
                print(access_url)
                instance.image = access_url


class NewsAdminForm(forms.ModelForm):
    #define image upload filed
    image_upload = forms.ImageField(required=True)

    class Meta:
        #define what model
        model = News
        fields = ['content', 'heading', 'date', 'image'] # Specify model fields to be included in the form
    
    def save(self, commit= True):
        instance = super().save(commit=False) # Calls super().save(commit=False) to create an instance of the model without committing it to the database yet.

        imageUploadingCloudFlare(self, instance)
        
        if commit:
            instance.save()

        return instance

class FeaturesAdminForm(forms.ModelForm):
    #define image upload filed
    image_upload = forms.ImageField(required=True)

    class Meta:
        #define what model
        model = Features
        fields = ['content', 'heading', 'date', 'image'] # Specify model fields to be included in the form
    
    def save(self, commit= True):
        instance = super().save(commit=False) # Calls super().save(commit=False) to create an instance of the model without committing it to the database yet.

        imageUploadingCloudFlare(self, instance)
        
        if commit:
            instance.save()

        return instance

class PhotoStoryAdminForm(forms.ModelForm):
    #define image upload filed
    image_upload = forms.ImageField(required=True)

    class Meta:
        #define what model
        model = PhotoStory
        fields = ['content', 'heading', 'date', 'image'] # Specify model fields to be included in the form
    
    def save(self, commit= True):
        instance = super().save(commit=False) # Calls super().save(commit=False) to create an instance of the model without committing it to the database yet.

        imageUploadingCloudFlare(self, instance)
        
        if commit:
            instance.save()

        return instance

class SocialJournalismAdminForm(forms.ModelForm):
    #define image upload filed
    image_upload = forms.ImageField(required=True)

    class Meta:
        #define what model
        model = SocialJournalism
        fields = ['content', 'heading', 'date', 'image'] # Specify model fields to be included in the form
    
    def save(self, commit= True):
        instance = super().save(commit=False) # Calls super().save(commit=False) to create an instance of the model without committing it to the database yet.

        imageUploadingCloudFlare(self, instance)
        
        if commit:
            instance.save()

        return instance

class SportsAdminForm(forms.ModelForm):
    #define image upload filed
    image_upload = forms.ImageField(required=True)

    class Meta:
        #define what model
        model = Sports
        fields = ['content', 'heading', 'date', 'image'] # Specify model fields to be included in the form
    
    def save(self, commit= True):
        instance = super().save(commit=False) # Calls super().save(commit=False) to create an instance of the model without committing it to the database yet.

        imageUploadingCloudFlare(self, instance)
        
        if commit:
            instance.save()

        return instance