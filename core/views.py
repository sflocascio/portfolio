from django.shortcuts import render

# Create your views here.


def index (request):
    return render(request, 'index07.html')

def post (request):
    return render(request, 'post.html')


def elements (request):
    return render(request, 'elements.html')