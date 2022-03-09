#created by Uman Sheikh

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyz(request):
    djtext = request.POST.get('text', 'default')
    count = 0
    analyzed = ""
    up = request.POST.get('upper', 'off')
    ginti = request.POST.get('count', 'off')

    if up == 'on':
        analyzed = djtext.upper()
    if ginti == 'on':
        for char in djtext:
            count += 1
    

    param = {'analyz':analyzed, 'count':count}
    return render(request, 'analyz.html', param)
