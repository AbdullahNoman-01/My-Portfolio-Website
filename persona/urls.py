from django.urls import path
from .import views
urlpatterns = [
   path('', views.Personal_info, name = 'info'),
]