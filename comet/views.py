from django.shortcuts import render
from django.http import HttpResponse


def basic(request):
    request.session["img"] = 0
    return render(request, "basic.html")


def new_sse(request):
    request.session["img"] += 1
    if request.session["img"] > 3:
        request.session["img"] = 1
    string = "/static/" + str(request.session["img"]) + ".jpg"
    retry = "retry: 3000\n\n"
    data = "data: %s\n\n" % string
    return HttpResponse(retry + data, content_type="text/event-stream")
