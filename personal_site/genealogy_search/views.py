from django.http import HttpResponse
from django.template import loader

def genealogy(request):
    template = loader.get_template('genealogy.html')
    return HttpResponse(template.render())

def search(request):
    try:
        collection = int(request.GET.get('collection'))
    except:
        collection = None
    template = loader.get_template('search.html')
    return HttpResponse(template.render(context={'collection': collection}))

def trees(request, slug):
    template = loader.get_template('trees.html')
    return HttpResponse(template.render(context={'slug': slug}))

def results(request):
    template = loader.get_template('results.html')
    return HttpResponse(template.render())

def record(request, collection_id, record_id):
    template = loader.get_template('record.html')
    return HttpResponse(template.render(context={'collection_id': collection_id, 'record_id': record_id}))
