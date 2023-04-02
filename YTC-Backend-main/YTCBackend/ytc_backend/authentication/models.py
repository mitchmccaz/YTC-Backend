from collections import UserDict
from django.db import models

# Create your models here.

class Song(models.Model):
    user = models.ForeignKey(UserDict, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField()

    def __str__(self):
        return self.title