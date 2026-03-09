from django.shortcuts import render, get_object_or_404, redirect
from .models import Resume
from .forms import ResumeForm

def resume_list(request):
    resumes = Resume.objects.all()
    return render(request, 'resumes/resume_list.html', {'resumes': resumes})

def resume_detail(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    return render(request, 'resumes/resume_detail.html', {'resume': resume})

def resume_upload(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resume_list')
    else:
        form = ResumeForm()
    return render(request, 'resumes/resume_upload.html', {'form': form})