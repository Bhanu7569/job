from django.db import models
from django.utils.text import slugify

class JobPost(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='company_logos/')
    description = models.TextField()
    responsibilities = models.TextField()
    skills_required = models.TextField()
    apply_link = models.URLField()
    posted_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            new_slug = base_slug
            counter = 1
            while JobPost.objects.filter(slug=new_slug).exclude(id=self.id).exists():
                new_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = new_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} at {self.company}"
