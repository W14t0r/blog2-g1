from django.shortcuts import render

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