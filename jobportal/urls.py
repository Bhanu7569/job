from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import StaticViewSitemap, JobPostSitemap  # use 'core', not 'jobs'
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

# Define sitemaps
sitemaps = {
    'static': StaticViewSitemap,
    'jobs': JobPostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),

    # Serve robots.txt
    path("robots.txt", TemplateView.as_view(
        template_name="robots.txt",
        content_type="text/plain"
    )),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
