from __future__ import unicode_literals

from datetime import datetime
from time import time
from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=200)
    videoid = models.BigAutoField(primary_key=True)
    like = models.BigIntegerField(default=0)
    dislike = models.BigIntegerField(default=0)
    viewCount = models.BigIntegerField(default=0)
    category = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    description = models.TextField()
    video_url = models.TextField(default="null")
    image_url = models.TextField(default="null")
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    duration=models.TextField(default="02:30")
    class Meta:
        db_table = "video"

    def __str__(self):
        return self.title


class User(models.Model):
    id=models.AutoField(primary_key=True)
    video=models.ForeignKey(Video,default=1)
    first = models.CharField(max_length=200)
    last = models.CharField(max_length=200)
    picture = models.TextField()
    email = models.EmailField()
    password = models.TextField()
    User_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        db_table = "User"

    def __str__(self):
        return self.title