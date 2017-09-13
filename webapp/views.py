from django.shortcuts import render
from django.http import HttpResponse
 

def index(request):
    context = {'data':'Its all about the game now you play it'}
    return render(request, 'index.html',context)