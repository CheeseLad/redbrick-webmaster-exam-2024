from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def confirm(request):
    return render(request, 'confirm.html')