from django.http import HttpResponse
from django.shortcuts import render
from meetings.models import Meeting


def welcome(request):
    return render(request, "website_templates/welcome.html", {'meetings':Meeting.objects.all()})


def about(request):
    return HttpResponse("This is about page")