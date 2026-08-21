from django.urls import path
from .import views
urlpatterns = [
   path('', views.Credentials, name='credenrials'),
]