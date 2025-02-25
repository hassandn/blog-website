from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'datetime_created', 'author')
    list_filter = ('status', 'datetime_created', 'author')


admin.site.register(Post, PostAdmin)
