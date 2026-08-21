from django.contrib import admin
from .models import Tag, Post, Like, Bookmark


class TagAdmin(admin.ModelAdmin):
    exclude = ('slug',)


class PostAdmin(admin.ModelAdmin):
    exclude = ('slug',)


admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Like)
admin.site.register(Bookmark)