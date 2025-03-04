from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'datetime_created', 'author')
    list_filter = ('status', 'datetime_created', 'author')
    ordering = ('-datetime_created', )
