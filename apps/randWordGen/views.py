from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
import random

# Create your views here.
def randWord():
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
               "V", "W", "X", "Y", "Z", "0", "2", "3", "4", "5", "6", "7", "8", "9"]
    ranWord = letters[random.randint(0, len(letters)-1)]
    for idx in range(13):
        ranWord += letters[random.randint(0, len(letters)-1)]
    return ranWord

def index(request):
    if 'randWord' not in request.session:
        request.session['randWord'] = ""
    request.session['randWord'] = randWord()
    if 'count' not in request.session:
        request.session['count'] = 1
    request.session['count'] += 1
    return render(request, 'randWordGen/index.html', request.session)

def increment(request):
    return index(request)