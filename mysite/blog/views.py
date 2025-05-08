# Create your views here.


from django.shortcuts import render


def index(request):
    return render(request, 'blog/index.html')



def blog1(request):
    return render(request, 'blog/blog1.html')

def blog2(request):
    return render(request, 'blog/blog2.html')

def blog3(request):
    return render(request, 'blog/blog3.html')

def blog4(request):
    return render(request, 'blog/blog4.html')


