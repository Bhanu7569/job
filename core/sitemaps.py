from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import JobPost   

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ['job_list', 'contact']

    def location(self, item):
        # Use full www URL for canonical purposes
        return f"https://www.jobifyworld.com{reverse(item)}"

class JobPostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return JobPost.objects.all()

    def location(self, obj):
        # Use full www URL for canonical purposes
        return f"https://www.jobifyworld.com{reverse('job_detail', args=[obj.slug])}"
