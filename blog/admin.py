from django.contrib import admin

# Register your models here.
from .models import Post, Rating, Restaurant

admin.site.register(Post)
admin.site.register(Rating)
admin.site.register(Restaurant)
