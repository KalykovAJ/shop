from django.shortcuts import render


def index(request):
    context = {
        "title": "Home - главная",
        "description": "Магазин мебели HOME",
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        "title": "Home - О нас",
        "description": "О нас",
    }
    return render(request, 'main/about.html', context)