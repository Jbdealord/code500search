from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Meta
from django.utils.html import strip_tags

def post_list_view(request):

    meta = Meta ()
    meta.title = 'Code 500'
    meta.url = 'https://code500.info'
    meta.image = 'https://code500.info/media/thumb/logo128.jpg'
    meta.body = 'Code 500 | Love code - but not only about Code'

    list_objects = Post.published.all()
    paginator = Paginator(list_objects, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'posts': posts, 'meta': meta})

def post_detail_view(request, post):
    post = get_object_or_404(Post, slug=post, status='published')

    meta = Meta ()
    meta.title = post.title
    meta.url = post.get_absolute_url
    meta.image = post.thumb.url
    meta.body = strip_tags(post.body)

    return render(request, 'blog/post/detail.html', {'post': post, 'meta': meta})