from django.http import HttpResponse
from django.shortcuts import render

from frontend.models import Course, Language


def index(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        languages = Language.objects.all()
        context = {
            'courses': courses,
            'languages': languages
        }
        return render(request, 'frontend/index.html', context)

    elif request.method == 'POST':
        languages = request.POST.getlist('language')
        languages = list(map(int, languages))
        courses = Course.objects.filter(language__in=languages).distinct()
        languages = Language.objects.all()
        context = {
            'courses': courses,
            'languages': languages
        }
        return render(request, 'frontend/index.html', context)
