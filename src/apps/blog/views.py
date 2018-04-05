from django.shortcuts import render
# from .models import Category


def home(request):
    name = 'Rafael Ribeiro'
    languages = ['Python', 'PHP', 'Java', 'Ruby']

    context = {
        'name': name,
        'languages': languages,
    }

    # Category.objects.create(name="Python")
    return render(request, 'home.html', context)
