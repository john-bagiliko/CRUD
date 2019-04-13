from django.contrib import admin

from .models import Post #add this to import the Post model

admin.site.register(Post) #add this to register the Post model

