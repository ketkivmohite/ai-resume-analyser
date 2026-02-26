from django.shortcuts import render
from .models import Resume 
from django.shortcuts import render, get_object_or_404

# Create your views here.
def resume_list(request):
    resumes = Resume.objects.all()
    return render(request, 'resumes/resume_list.html', {'resumes': resumes})

def resume_detail(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    return render(request, 'resumes/resume_detail.html', {'resume': resume})