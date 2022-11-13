from django.contrib import admin

# Register your models here.

from .models import Post, Category, Comment, Profile, PostView, Like

#admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(PostView)
admin.site.register(Like)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'status','author')


@admin.register(Comment)
class ComentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'content','timestamp')
