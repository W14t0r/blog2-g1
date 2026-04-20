from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render
from blog.models import Post

def post_list(request):
    posts = Post.published.all()
    return render(
        request,
        template_name='blog/post/list.html',
        context={'posts': posts}
    )

def post_detail(request, pk):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.html', context={'post': post})