from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def january(request):
    return HttpResponse("Spend At LEAST 5 minutes a day reading some books")


def february(reqeust):
    return HttpResponse("Walk At LEAST for 20 minutes every single day")
