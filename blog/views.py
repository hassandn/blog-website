from django.shortcuts import render
from .models import Post

def post_list_view(request):
    posts = Post.objects.all()
    context = {
        'posts_list': posts
    }
    return render(request, 'blog/posts_list.html', context)
