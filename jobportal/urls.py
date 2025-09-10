from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import StaticViewSitemap, JobPostSitemap  # use 'core', not 'jobs'
from django.conf import settings
from django.conf.urls.static import static


sitemaps = {
    'static': StaticViewSitemap,
    'jobs': JobPostSitemap,   # <-- updated name
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
