from django.urls import path
# from mysite.views import import http_test
# from .views import import http_test
from website.views import *
urlpatterns = [
    # Path ('url address', 'view', name)
    # path('home', index_view),
    path('', index_view), # => Main Page
    path('about', about_view),
    path('contact', contact_view)
]