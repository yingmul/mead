from django.template import Context, loader
from django.http import HttpResponse

from schools.models import School

#TODO make this into a view class, change schools/index.html to use sitebase
def index(request):
    schools = School.objects.all()
    context = Context({
        'schools': schools
    })
    t = loader.get_template('schools/index.html')
    return HttpResponse(t.render(context))