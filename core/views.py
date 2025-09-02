
from django.shortcuts import render, get_object_or_404
from .models import JobPost

def job_list(request):
    jobs = JobPost.objects.all().order_by('-posted_at')
    return render(request, 'core/job_list.html', {'jobs': jobs})


def job_detail(request, slug):
    job = get_object_or_404(JobPost, slug=slug)
    skills = [s.strip() for s in job.skills_required.split(',')]
    return render(request, 'core/job_detail.html', {'job': job, 'skills': skills})



def contact(request):
    return render(request, 'core/contact.html')