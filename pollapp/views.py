from django.http import HttpResponse
import datetime
from django.shortcuts import render


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def home(request):
	now = datetime.datetime.now()
	context = {'datetime_now' :now}
	return render(request, 'home.html' ,context)      