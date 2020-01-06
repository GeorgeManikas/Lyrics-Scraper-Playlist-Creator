from django.db import models
from django.contrib.auth.models import User
class Playlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    artist = models.CharField(max_length=40,default='No artist')
    title = models.CharField(max_length=40, default='No song title')
    lyrics = models.TextField(default='No lyrics Found')

    def __str__(self):
        return(f'Artist:{self.artist}, Song:{self.title}')

    
    
    