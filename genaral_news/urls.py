from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('preview/', views.previewGenarator, name='preview Genarate')
]