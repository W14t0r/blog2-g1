from django.contrib import admin
from blog.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish', 'author']
    list_filter = ['status', 'publish', 'created', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
