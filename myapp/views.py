from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
# Create your views here.

def show_home_page(request):
    category = Category.objects.all()
    images = Image.objects.all()
    data = {"images":images, 'category':category}
    return render(request, 'home.html', data)

def show_category(request, cid):
    category = Category.objects.all()
    cats = Category.objects.get(pk = cid)
    images = Image.objects.filter(cat = cats)
    data = {"images":images, 'category':category}
    return render(request, 'home.html', data)

def home(request):
    return redirect('/show_home_page')

