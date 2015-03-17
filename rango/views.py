from django.shortcuts import render
from rango.models import Category
# from django.http import HttpResponse

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context_dict)

def about(request):
    context_text = {"about_message": "Rango says here is the about page"}
    return render(request, 'rango/about.html', context_text)

def flot(request):
    return render(request, 'rango/flot.html')
