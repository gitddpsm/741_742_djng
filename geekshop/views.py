from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'geekshop/index.html')


def contact(request):
    return render(request, 'geekshop/contact.html')
