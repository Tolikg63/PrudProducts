from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Dishes

def index(request):
    categories = Category.objects.all()
    return render(request, 'shop/home_page.html', {'categories': categories})


def category_dishes(request, category_id):
    dishes = Dishes.objects.filter(category_id=category_id)
    return render(request, 'shop/category_dishes.html', {'dishes': dishes})


def bestsellers(request):
    categories = Category.objects.all()
    return render(request, 'shop/bestsellers.html', {'categories': categories})


def news(request):
    categories = Category.objects.all()
    return render(request, 'shop/news.html', {'categories': categories})