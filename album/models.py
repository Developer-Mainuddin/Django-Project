from django.db import models
from django.db.models.fields import TextField

# Create your models here.

class Album(models.Model):

    thumbnail = models.ImageField(upload_to='dev_mainuddin_album/photo/')
    description = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)



    
