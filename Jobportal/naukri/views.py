from django.shortcuts import render
from naukri.models import Mumbai, Pune, Bengaluru

# Create your views here.

def home_view(request):
    return render(request, 'naukri/home.html')

def mumbai_view(request):
    job_list = Mumbai.objects.all()
    return render(request, 'naukri/mumbai.html', {'job_list': job_list})

def pune_view(request):
    job_list = Mumbai.objects.all()
    return render(request, 'naukri/pune.html', {'job_list': job_list})

def bengaluru_view(request):
    job_list = Bengaluru.objects.all()
    return render(request, 'naukri/bengaluru.html', {'job_list': job_list})