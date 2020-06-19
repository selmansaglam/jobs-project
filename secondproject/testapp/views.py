from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.


def date_time_view(request):
    date = datetime.datetime.now()
    s = '<h3>The current date and time at server is '+str(date)+'</h3>'
    return HttpResponse(s)
