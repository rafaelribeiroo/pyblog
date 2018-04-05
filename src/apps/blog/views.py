from django.shortcuts import render
from .models import Category


def home(request):
    name = 'Rafael Ribeiro'
    languages = ['Python', 'PHP', 'Java', 'Ruby']

    # Category.objects.create(name="Python");
    categories = Category.objects.all()

    context = {
        'name': name,
        'languages': languages,
        'categories': categories,
    }

    return render(request, 'home.html', context)
