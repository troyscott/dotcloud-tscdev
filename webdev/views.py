from django.http import HttpResponse


def index(request):
	return HttpRequest('hello world')


