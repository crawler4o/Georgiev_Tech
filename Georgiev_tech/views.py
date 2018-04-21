from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

def chat_bot(request):
    return HttpResponse('Chat Bot')

def bulls_and_cows(request):
    return HttpResponse('bulls_and_cows')

def csv_to_xlsx(request):
    return HttpResponse('csv_to_xlsx')

def mercury_retrograde(request):
    return HttpResponse('mercury_retrograde')
