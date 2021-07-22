from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'slogan': 'Сидеть не пересидеть!',
        'header': request.headers
    }
    # print(context)
    return render(request, 'geekshop/index.html', context)


def contact(request):
    return render(request, 'geekshop/contact.html')
