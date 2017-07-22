from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
def index(request):
    if request.method == 'POST':
        errors = Course.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
        else:
            User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = request.POST['password'],)
            return redirect('/')
    else:
        context = {
        'courses': Course.objects.all()
        }
        return render(request, 'course/index.html', context)
def remove(request, course_id):
    if request.method == 'POST':
        Course.objects.get(id = course_id).delete()
        return redirect('/')
    else:
        context = {
        'courses': Course.objects.get(id = course_id)
        }
        return render(request, 'course/remove.html', context)
