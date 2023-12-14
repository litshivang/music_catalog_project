# tracks/models.py
from django.db import models
from albums.models import Album

class Track(models.Model):
    title = models.CharField(max_length=255)
    duration = models.DurationField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
