# Create your views here.
from django.template import Template, Context
from django.shortcuts import render_to_response


def feed(request):

	return render_to_response('usgs.html')



