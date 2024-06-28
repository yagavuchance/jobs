from django.shortcuts import render
from jobs.models import Jobs
from scholarship.models import Scholarship
from fellowships.models import Fellowship

# Create your views here.

def index(request):
    jobs_list = Jobs.objects.all()[:4]
    scholarship_list = Scholarship.objects.all()[:5]
    fellowship_list = Fellowship.objects.all()[:5]
    context= {
        'jobs_list': jobs_list,
        'scholarship_list': scholarship_list,
        'fellowship_list': fellowship_list
    }
    return render(request,'cores/index.html',context)

def about(request):
    return render(request,'cores/about.html')
