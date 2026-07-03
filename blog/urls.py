from django.urls import path
from blog.views import *

app_name='blog'

urlpatterns=[
    path('', blog_view, name='index'),
    path('single', blog_single, name='single'),

    """
    path('<str:name>/lastname/<str:family_name>/age/<int:age>',
    # dynamic URL patterns with three dynamic segments:
    # <str:name>          => captures a string, passed to view as 'name'
    # <str:family_name>   => captures a string, passed to view as 'family_name'
    # <int:age>           => captures an integer, passed to view as 'age'
    static URL patterns: /john/lastname/doe/age/25
    
    test,
    # view function that will receive name, family_name and age as arguments
    
    name='test'
    # name of this URL pattern, used for reverse URL lookups (e.g. {% url 'test' %})
    )
    """
    
    """
    path('post-<int:pid>', test, name='post-test'),
    # URL pattern with a literal prefix "post-" followed by a dynamic integer segment
    # <int:pid>  => captures an integer, passed to the view as 'pid'
    # example match: /post-5  =>  pid=5
    """
]