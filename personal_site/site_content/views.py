from django.http import HttpResponse
from django.template import loader

def homepage(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

def fifteen(request):
    template = loader.get_template('fifteen.html')
    return HttpResponse(template.render())

def games(request):
    template = loader.get_template('games.html')
    return HttpResponse(template.render())

def twixt(request):
    template = loader.get_template('twixt.html')
    return HttpResponse(template.render())

def rubiks(request):
    template = loader.get_template('rubiks.html')
    return HttpResponse(template.render())

def phil_theo(request):
    template = loader.get_template('phil-theo.html')
    return HttpResponse(template.render())

def services(request):
    template = loader.get_template('services.html')
    return HttpResponse(template.render())
