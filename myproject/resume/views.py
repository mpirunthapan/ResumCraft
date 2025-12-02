from django.shortcuts import render
from .forms import ProfileForm
from .models import Profile

# Create your views here.
def index(request):
    return render(request, 'index.html')

def accept(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "index.html")  # create this page
    else:
        form = ProfileForm()

    return render(request, "accept.html", {"form": form})

def preview(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    return render(request, "preview.html", {"profile": profile})