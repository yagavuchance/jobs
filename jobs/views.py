from django.shortcuts import render
from .models import Jobs

# Create your views here.

def jobs(request):
    jobs_list = Jobs.objects.all()
    context= {
        'jobs_list': jobs_list
    }
    return render(request,'lists-jobs/jobs.html',context)
