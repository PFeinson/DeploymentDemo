from django.shortcuts import render, HttpResponse, redirect
from ..loginAndReg.models import User
# Create your views here.
def index(request):
    return render(request, 'loginAndReg/index.html')

def validate(request):
    responseFromModels = User.users.validateAndRegisterData(request.POST)
    if responseFromModels['status']:
        request.session['user'] = responseFromModels['user'].first_name
        return success(request)
    else:
        for error in responseFromModels['errors']:
            print error

        return index(request)

def login(request):
    responseFromModels = User.users.login(request.POST)
    if responseFromModels['status']:
        request.session['user'] = responseFromModels['user'].first_name
        return success(request)
    else:
        print responseFromModels['errors']
        return index(request)

def success(request):
    if not 'user' in request.session:
        index(request)
    return redirect('/courses')
    #return render(request, 'loginAndReg/success.html', request.session)

