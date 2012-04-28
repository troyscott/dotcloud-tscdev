# Create your views here.
from django.http import HttpResponse


def feed(request):
	return HttpResponse('This is the usgs feed...')




