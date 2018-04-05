from django.shortcuts import render
from .models import Category


def home(request):
    name = 'Rafael Ribeiro'
    # languages = ['PHP', 'Java', 'Ruby', 'Go']
    # for category in languages:
    #     Category.objects.create(name=category)

    # Category.objects.create(name="Python")
    # categories = Category.objects.filter(name="Java").delete()
    all_categories = Category.objects.all()

    context = {
        'name': name,
        'categories': all_categories,
    }

    return render(request, 'home.html', context)
