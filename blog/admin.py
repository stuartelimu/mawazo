from django.contrib import admin
from .models import Author, Comment, Post, PostView

admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Post)

