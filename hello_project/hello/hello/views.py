from django.http import HttpResponse
from django.shortcuts import render

from jabbalib import myhash


def index(request):
    name = 'Jabba'
    context = {
        'name': name,
        'md5': myhash.string_to_md5(name),
        'list': [2, "3", False, None, 3.14],
    }
    return render(request, 'hello/index.html', context)


#def about(request):
#    return HttpResponse("about")


def about(request):
    return render(request, 'hello/about.html')
