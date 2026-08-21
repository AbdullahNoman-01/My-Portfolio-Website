from django.shortcuts import render

# Create your views here.
def Personal_info(request):
   return render(request, 'persona/personal_info.html')