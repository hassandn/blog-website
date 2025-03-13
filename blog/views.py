from django.shortcuts import render
from .models import Post

def post_list_view(request):
    posts = Post.objects.all()
    context = {
        'posts_list': posts
    }
    return render(request, 'blog/posts_list.html', context)

def post_detail_view(request, pk):

    post = Post.objects.get(pk=pk)
    context = {
        "post" : post,
    }
    return  render(request=request, template_name= "blog/post_detail.html", context=context, status=200)

