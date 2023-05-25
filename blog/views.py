from django.shortcuts import render

def blog_home(request):
    # Add your view logic here
    return render(request, 'blog/home.html')
