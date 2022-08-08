from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile


def profiles_db(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles.profiles_page.html', {'profiles': profiles})