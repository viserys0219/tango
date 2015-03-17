from django.shortcuts import render
# from django.http import HttpResponse

def index(request):
    context_text = {"boldmessage": "I am bold font from the context"}
    return render(request, 'rango/index.html', context_text)

def about(request):
    context_text = {"about_message": "Rango says here is the about page"}
    return render(request, 'rango/about.html', context_text)

def flot(request):
    return render(request, 'rango/flot.html')
