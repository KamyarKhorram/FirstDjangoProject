from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.
def blog_view(request):
    posts=Post.objects.filter(status=1)
    context={"posts":posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    # Method 1
    # post=get_object_or_404(Post, pk=pid, status=1)

    # Method 2 (recommended)
    posts=Post.objects.filter(status=1)
    post=get_object_or_404(posts, pk=pid)
    context={'post':post}
    return render(request, 'blog/blog-single.html', context)

"""
def test(request, name, family_name, age): # name, family_name, age come from the URL path parameters

    context={'name':name, 'family_name':family_name, 'age':age}
    # pass captured values to the template as context
    
    return render(request, 'test.html', context)
"""

"""
def test2(request, pid): # pid comes from the URL, e.g. path('post/<int:pid>/', test2, name='test2') so visiting /post/5/ passes pid=5 into this view

    ## Method 1
    #### post=Post.objects.get(id=pid)
    # raw approach: if no Post with this id exists, Django raises
    # a DoesNotExist exception and the user sees an ugly 500 server error
    
    ## Method 2 (recommended)
    post=get_object_or_404(Post, pk=pid)
    # safer shortcut provided by Django:
    # - if the post exists  => returns it, just like .get()
    # - if it doesn't exist => raises Http404 instead, showing a clean
    # "Not Found" page rather than crashing the app

    context={'post':post}
    # pass the retrieved post object to the template
    
    return render(request, 'test.html', context)
"""
