from django.contrib import admin

from .models import BlogTopic, BlogPost

# Register your models here.
admin.site.register(BlogTopic)
admin.site.register(BlogPost)