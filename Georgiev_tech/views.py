from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
from random import randrange
import requests

def home(request):
    return render(request, 'index.html')

def jokes(request):

    def parser(url):
    	r = requests.get(url)
    	soup = BeautifulSoup(r.text, "html.parser")
    	return soup

    def writer(soup):
        jokes = []
        for x in soup.find_all(class_="joke-text"):
            jokes.append(x.text + "\n")
        return jokes

    jokes = writer(parser('http://www.laughfactory.com/jokes/technology-jokes'))
    rand_joke = jokes[randrange(len(jokes))]

    return render(request, 'jokes.html', {'rand_joke':rand_joke})


def bulls_and_cows(request):
    return HttpResponse('bulls_and_cows')

def csv_to_xlsx(request):
    return HttpResponse('csv_to_xlsx')

def mercury_retrograde(request):
    return HttpResponse('mercury_retrograde')
