from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, kitob
app_name = 'polls'


urlpatterns = [
    path('', index, name='index'),
    path('kitoblar/<int:kitob_id>/', kitob, name='kitoblar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
