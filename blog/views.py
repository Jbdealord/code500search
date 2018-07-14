from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

def post_list_view(request):
    list_objects = Post.published.all()
    paginator = Paginator(list_objects, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail_view(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    return render(request, 'blog/post/detail.html', {'post': post})