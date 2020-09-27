from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=50)


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="courses", default="none/nothumb.jpg")
    language = models.ManyToManyField(Language)


class Rating(models.Model):
    RATING = [
        ('Bad', '1'),
        ('Average', '2'),
        ('Good', '3'),
        ('Excellent', '4'),
        ('Best', '5')
    ]
    mark = models.CharField(default=None, max_length=100, choices=RATING)