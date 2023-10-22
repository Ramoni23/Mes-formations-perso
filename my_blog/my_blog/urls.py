from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from blog.views import home, detail

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include("blog.urls")),
    path('', home, name="home"),
    path('article/<int:id_article>', detail, name="detail"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
