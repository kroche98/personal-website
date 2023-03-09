from django.http import HttpResponse
from django.template import loader

def homepage(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render(context={'active_page':'homepage'}))

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render(context={'active_page':'contact'}))

def fifteen(request):
    template = loader.get_template('fifteen.html')
    return HttpResponse(template.render(context={'active_page':'games'}))

def games(request):
    template = loader.get_template('games.html')
    return HttpResponse(template.render(context={'active_page':'games'}))

def twixt(request):
    template = loader.get_template('twixt.html')
    return HttpResponse(template.render(context={'active_page':'games'}))

def rubiks(request):
    template = loader.get_template('rubiks.html')
    return HttpResponse(template.render(context={'active_page':'games'}))

def phil_theo(request):
    template = loader.get_template('phil-theo.html')
    return HttpResponse(template.render(context={'active_page':'phil-theo'}))

def services(request):
    template = loader.get_template('services.html')
    return HttpResponse(template.render(context={'active_page':'services'}))
