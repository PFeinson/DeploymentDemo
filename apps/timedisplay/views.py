from django.shortcuts import render, HttpResponse
from datetime import datetime
import arrow
# Create your views here.
def index(request):
    curTime = arrow.now().format('MMM DD, YYYY') + "\n" + arrow.now().format('HH:MM:SS A')
    data = dict(currentTimeAndDate=curTime)
    return render(request, 'timedisplay/index.html', data)