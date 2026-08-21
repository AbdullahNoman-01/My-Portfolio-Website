from django.shortcuts import render,get_object_or_404
from .import models
# Create your views here.

def Fake_Project(request):
   projects = models.Project.objects.all()

   return render(request, 'project/project.html',{'projects':projects})

def Project_Details(request, id):
   project = get_object_or_404(models.Project, id =id)

   return render(request,'project/project_detail.html',{'project':project})