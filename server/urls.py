
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from server import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name = 'index.html')),
]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.OUTPUT_URL, document_root=settings.OUTPUT_ROOT)

