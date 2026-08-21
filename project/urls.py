from django.urls import path
from .import views
urlpatterns = [
   path('', views.Fake_Project, name='project'),
   path('project-detail/<int:id>/', views.Project_Details, name='project_detail'),
]