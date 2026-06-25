from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# def index_view(request):
#     return render(request, 'index.html') # => request کاربر

# داخل folder
def index_view(request):
    return render(request, 'website/index.html') # => request کاربر

# def about_view(request):
# #     return HttpResponse('<h1>About Page</h1>')

# داخل folder
def about_view(request):
    return render(request, 'website/about.html') # => request کاربر

# def contact_view(request):
#     return HttpResponse('<h1>Contact Page</h1>')

def contact_view(request):
    return render(request, 'contact.html') # => request کاربر

