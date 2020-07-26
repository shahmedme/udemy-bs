from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=50)


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="courses", default="none/nothumb.jpg")
    language = models.ManyToManyField(Language)