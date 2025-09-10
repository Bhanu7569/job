from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import JobPost   

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ['job_list', 'contact']

    def location(self, item):
        return reverse(item)

class JobPostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return JobPost.objects.all()

    def location(self, obj):
        return reverse('job_detail', args=[obj.slug])
