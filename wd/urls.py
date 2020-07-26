from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from frontend import views as frontend_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontend_views.index)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
