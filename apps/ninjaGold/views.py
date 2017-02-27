from django.shortcuts import render, HttpResponse, redirect
import random

# Create your views here.
def index(request):
    confirmSessions(request)
    return render(request, 'ninjaGold/index.html', request.session)

def compute(request, local):
    confirmSessions(request)
    request.session['gold'] += computeGold(request, local)
    print request.session['gold']
    return index(request)

def computeGold(request, local):
    if local == 'farm':
        randNum = random.randint(10, 20)
        request.session['activities'] += ("<p class = 'green'>" + "Earned " + str(randNum) +
                                         "gold. You have a total of " + str(request.session['gold']) + "</p>")
        return randNum
    elif local == 'cave':
        randNum = random.randint(5, 10)
        request.session['activities'] += ("<p class = 'green'>" + "Earned " + str(randNum) +
                                         "gold. You have a total of " + str(request.session['gold']) + "</p>")
        return randNum
    elif local == 'house':
        randNum = random.randint(2, 5)
        request.session['activities'] += ("<p class = 'green'>" + "Earned " + str(randNum) +
                                         "gold. You have a total of " + str(request.session['gold']) + "</p>")
        return randNum
    elif local == 'casino':
        randNum = random.randint(-50, 50)
        if (randNum > 0):
            request.session['activities'] += ("<p class = 'green'>" + "Earned " + str(randNum) +
                                              "gold. You have a total of " + str(request.session['gold']) + "</p>")
            return randNum
        else:
            request.session['activities'] += ("<p class = 'red'>" + "Lost " + str(randNum) +
                                              "gold. You have a total of " + str(request.session['gold']) + "</p>")
            return randNum
    else:
        return 0

def confirmSessions(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = ""
def reset(request):
    if 'gold' in request.session:
        request.session['gold'] = 0
    if 'activities' in request.session:
        request.session['activities'] = ""

    return index(request)