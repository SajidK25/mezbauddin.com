from django.shortcuts import render

def home(request):
    # Add your view logic here

    return render(request, 'web/home.html')
