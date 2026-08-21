from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HOME, name='home'),
    path('project/', include('project.urls')),
    path('credentials/', include('credentials.urls')),
    path('persona/', include('persona.urls')),
    path('stream/', include('stream.urls')),
]


urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)