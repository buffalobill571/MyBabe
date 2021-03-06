from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book
from .forms import ContactForm
from django.core.mail import send_mail


def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        elif len(q) > 20:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            message = 'You searched for %r' % request.GET['q']
            return render(request, 'search_results.html',
                          {'books': books, 'query': q})
    return render(request, "search_form.html", {'error': error})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', "noreply@example.com"),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect("/blog/thanks/")
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!'}
        )
    return render(request, "contact_form.html", {'form': form})
