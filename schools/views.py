from django.template import Context, loader
from django.http import HttpResponse

#TODO make this into a view class, change schools/index.html to use sitebase
def index(request):
    c = Context({})
    t = loader.get_template('schools/index.html')
    return HttpResponse(t.render(c))