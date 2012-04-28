from django.http import HttpResponse


def quake(request):
	return HttpResponse('hello world')


