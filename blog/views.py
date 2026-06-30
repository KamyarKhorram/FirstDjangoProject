from django.shortcuts import render


# Create your views here.
def blog_view(request):
    return render(request, 'blog/blog-home.html')


def blog_single(request):
    context = {'title': 'Cyrus can be a great destination for traveling in summer season!',
               'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet'
                          'atque corporis distinctio eum labore officiis perspiciatis'
                          'reiciendis rem unde vero? Accusantium adipisci architecto'
                          'at corporis delectus deleniti dolor ea eligendi explicabo,'
                          'fugiat illo, iure labore minus mollitia nemo neque quia,'
                          'recusandae ullam vel voluptatem! Ab, adipisci, magnam!'
                          'Labore, odit ullam!',
               'author': 'Kamyar Khorram'}
    return render(request, 'blog/blog-single.html', context)
