from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, per_page=4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts,
    }
    return render(request, 'blog/post/list.html', context)


def post_detail(request, slug, year, month, day):
    post = get_object_or_404(Post, slug=slug, status='published',
                             publish__year=year, publish__month=month, publish__day=day)
    context = {
        'post': post,
    }
    return render(request, 'blog/post/detail.html', context)
