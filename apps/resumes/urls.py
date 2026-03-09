from django.urls import path
from .views import resume_list
from . import views


urlpatterns = [
    path("", resume_list, name="resume_list"),
    path("<int:pk>/", views.resume_detail, name="resume_detail"),
    path('upload/', views.resume_upload, name='resume_upload'),
]