from django.db import models
class Post(models.Model):
 title = models.CharField(max_length=120, help_text='title of message.')
 message = models.TextField(help_text="what's on your mind ...")
 
 def __str__(self):
  return self.title