from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def show_test(request):
  return render(request, 'test.html')

def show_top(request):
  return render(request, 'top.html')

