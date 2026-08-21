from django.db import models

# Create your models here.
class Project(models.Model):
   image = models.ImageField(upload_to='project/', blank=True, null= True)
   title = models.CharField(max_length=200)
   description = models.TextField()
   technology = models.CharField(max_length=300)
   github_link = models.URLField(blank=True)
   def __str__(self):
       return self.title
   