from django.http import HttpResponse
from django.shortcuts import render

from profiles.models import Profile


def home(request):
    profiles = Profile.object.all()
    context = {
        'profiles': profiles,
    }
    return render(request, "home.html", context)