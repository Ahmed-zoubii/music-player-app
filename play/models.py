from django.contrib.auth.models import User
from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=128)
    artist = models.CharField(max_length=128)
    path_to_file = models.FileField(upload_to='media/')
    favorite_by = models.ManyToManyField(to=User, related_name='favorite_songs')