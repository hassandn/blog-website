from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

def post_list_view(request):
    posts = Post.objects.filter(status='pub')
    context = {
        'posts_list': posts
    }
    return render(request, 'blog/posts_list.html', context)

def post_detail_view(request, pk):
    
    # try:
    #     post = Post.objects.get(pk=pk)
    # except:
    #     post = None
    #     print("exception")
    # return  render(request=request, template_name= "blog/post_detail.html", context=context, status=200)

    # try:
    #     post = Post.objects.get(pk=pk)
    # except Post.DoesNotExist:
    #     post = None
    #     print("exception")
    # return  render(request=request, template_name= "blog/post_detail.html", context=context, status=200)

    # try:
    #     post = Post.objects.get(pk=pk)
    # except ObjectDoesNotExist:
    #     post = None
    #     print("exception")
    # return  render(request=request, template_name= "blog/post_detail.html", context=context, status=200)


    post = get_object_or_404(Post, pk=pk)
    context = {
        "post" : post,
    }
    
    
    return  render(request=request, template_name= "blog/post_detail.html", context=context, status=200)

