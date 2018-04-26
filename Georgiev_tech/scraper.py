import requests
from bs4 import BeautifulSoup
from random import randrange

def parser(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup

def writer(soup):
    jokes = []
    for x in soup.find_all(class_="joke-text"):
        jokes.append(x.text + "\n")
    return jokes

def say_a_joke():
    jokes = writer(parser('http://www.laughfactory.com/jokes/technology-jokes'))
    rand_joke = jokes[randrange(len(jokes))]
    return rand_joke
