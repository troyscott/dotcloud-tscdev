# Create your views here.
from django.template import Template, Context
from django.http import HttpResponse


def feed(request):
	return HttpResponse('This is the usgs feed')



