from django.shortcuts import render, HttpResponse, redirect
from ..coursesApp.models import course, User
from ..loginAndReg.models import User
from django.db.models import Count
from django.utils import timezone
# Create your views here.
context = {}
def index(request):
    #if 'courseCatalog' not in context:
    context['courseCatalog'] = course.objects.all()
    return render(request, 'CoursesApp/index.html', context)

def addCourse(request):
    newCourse = course.objects.create(course_name=request.POST['courseName'], course_description=request.POST['description'])
    newCourse.save()
    return redirect('/courses')

def deleteCourse(request, courseToDel):
    course.objects.all().filter(course_name=courseToDel).delete()
    return redirect('/courses')

def allCourses(request):
    context['allCurrentUsers'] = User.users.all()
    context['courseCatalog'] = course.objects.all().annotate(number_of_students = Count('all_users'))
    return render(request, 'CoursesApp/allCourses.html', context)

def addToCourse(request):
    #Fast Fail
    if 'usersList' not in request.POST or 'allCourses' not in request.POST:
        return redirect("/courses/allCourses")

    #Split apart user name from POST to use in a query
    userName = request.POST['usersList'].split("_")
    # Submit query to find user's database entry
    currentUser = User.users.get(first_name = userName[0], last_name = userName[1])
    # Submit query to select which course to add user to
    courseToAppend = course.objects.get(course_name = str(request.POST['allCourses']))
    # Add course to key
    courseToAppend.all_users.add(currentUser)

    return redirect('/courses/allCourses')