from django.shortcuts import render

# Create your views here.


def index (request):
    return render(request, 'index07.html')

def elements (request):
    return render(request, 'elements.html')

def portfolio (request):
    return render(request, 'portfolio.html')

def design (request):
    return render(request, 'design.html')

def works (request):
    return render(request, 'index08.html')

# Six Portfolio Detail Pages Below 

# post is the little triangle 
def post (request):
    return render(request, 'post.html')

def quizzer (request):
    return render(request, 'quizzer.html')

def oakhouse (request):
    return render(request, 'oakhouse.html')

def itunes (request):
    return render(request, 'itunes.html')

def chant(request):
    return render(request, 'chant.html')

def wayfinder (request):
    return render(request, 'wayfinder.html')



