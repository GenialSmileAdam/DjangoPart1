from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calculate():
    x = 29
    y= 17
    return x

def say_hello(request):
    return render(request, 'home.html',
                  {
                      'name':"Jason"
                  })