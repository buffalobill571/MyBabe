import datetime
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
import os


def hello(request):
    return HttpResponse("Hello World")


def current_time(request):
    print(request.path)
    now = datetime.datetime.now()
    html = """
    <html>
        <body>
            It's now %s
        </body>
    </html>
    """ % now
    return HttpResponse(html)


def hours_ahead(request, offset):
    print(request.path)
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = """
    <html>
        <body>
            It's after %d hours %s
        </body>
    </html>
    """ % (offset, dt)
    return HttpResponse(html)


def temp_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'mytemp', {'hours': offset, 'date': dt})


def just_meta(request):
    req = request.META
    string = ""
    for key in req:
        string = string + "%s : %s\n" % (key, req[key])
    return HttpResponse("%s" % (string))


def good_meta(request):
    values = request.META.items()
    values = sorted(values)
    html = []
    for k, v in values:
        html.append("""
        <tr>
            <td>%s</td>
            <td class='second'>%s</td>
        </tr>
        """ % (k, v))
    return HttpResponse("""
    <style>
        table tr td {
            border: solid black 1px;
            margin: 0;
            padding: 0;
            height: 30px;
        }
    </style>
        <table>
            %s
        </table>
    """ % "\n".join(html))
