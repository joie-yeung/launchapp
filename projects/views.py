from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponse
from .models import Project
# Create your views here.

def index(request):
    # return HttpResponse("Welcome to your projects!")
    project_list = Project.objects.order_by("-date")
    context = {"project_list": project_list}
    return render(request, "projects/index.html", context)

def description(request, proj_id):
    project = get_object_or_404(Project, pk=proj_id)
    return render(request, "projects/description.html", {"project": project})

