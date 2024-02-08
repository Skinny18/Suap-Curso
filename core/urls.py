from django.urls import path, include
from django.conf import settings
from core import views
from django.conf.urls.static import static

urlpatterns = [
    path('form/', views.get_name)   
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
