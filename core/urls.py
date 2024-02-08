from django.urls import path, include
from django.conf import settings
from core import views
from django.conf.urls.static import static

urlpatterns = [
    path('form', views.get_name, name='form'),  
    path('view', views.view_name, name='view'), 
    path('delete_user/<int:user_id>', views.delete_user, name='delete_user')

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
