from django.urls import path
# from mysite.views import import http_test
# from .views import import http_test
from website.views import *

app_name = 'website' # A connector between the interpreter and urls that this app contain (In some circumstances, when projects are more advanced, Name similarity between apps may occur)

urlpatterns = [
    # Path ('url address', 'view', name)
    # path('home', index_view),
    path('', index_view, name='index'), # => Main Page
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact')
]