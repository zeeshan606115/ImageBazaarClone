from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from wsgiref.util import FileWrapper
import mimetypes
import os
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



def download_image(request, image_id):
    img = Image.objects.get(id=image_id)
    wrapper = FileWrapper(open(img.file))  # img.file returns full path to the image
    content_type = mimetypes.guess_type(filename)[0]  # Use mimetypes to get file type
    response = HttpResponse(wrapper,content_type=content_type)
    response['Content-Length'] = os.path.getsize(img.file)
    response['Content-Disposition'] = "attachment; filename=%s" %  img.name
    return response

