from django.shortcuts import render

# Create your views here.
def Credentials(request):
   return render(request, 'credentials/credentials.html')