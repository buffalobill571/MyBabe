from django.shortcuts import render


def basic(request):
    return render(request, "parabellum.html", {"user": request.user, "ip": request.META["REMOTE_ADDR"]})


def xss(request):
    if request.method == "POST":
        return render(request, "get.html", {"q": request.POST["q"]})
    else:
        return render(request, "post.html")
