from django.contrib import admin

from .models import Course, Language, Rating

admin.site.register(Course)
admin.site.register(Language)
admin.site.register(Rating)
