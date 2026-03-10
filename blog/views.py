from django.shortcuts import render
from django.http import HttpResponse

def portao(request):
    return HttpResponse("Voce chegou ao portao da casa")

def sala(request):
    return HttpResponse("Voce chegou a sala")

def quarto(request):
    return HttpResponse("Voce chegou ao quarto")

def post_list(request):
    return render(request, 'blog/post_list.html', {})