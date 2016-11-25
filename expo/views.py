from django.shortcuts import render
from django.http import HttpResponse


def basic(request, var="myvar", extra="noooo"):
    return HttpResponse(var + extra)