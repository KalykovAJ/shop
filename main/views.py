from django.shortcuts import render
from goods.models import Category


def index(request):
    categories = Category.objects.all()
    context = {
        "title": "Home - главная",
        "content": "Магазин мебели HOME",
        "categories": categories
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        "title": "Home - О нас",
        "content": "О нас",
    }
    return render(request, 'main/about.html', context)