from django.shortcuts import render
from django.http import HttpResponse
import random as rand
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    password = ''
    length = int(request.GET.get('length'))
    numeric = list("1234567890")
    characters = []
    special_chars = list('!@#$%^&*()_+=')
    if request.GET.get('LowerCase'):
        characters.extend(list("abcdefghijklmnopqrstuvwxyz"))
    if request.GET.get('UpperCase'):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUWXYZ"))
    if request.GET.get('Special'):
        characters.extend(special_chars)
    if request.GET.get('Numbers'):
        characters.extend(numeric)
    for num in range(length):
        password += rand.choice(characters)
    return render(request, 'generator/password.html', {"password": password})

def readme(request):
    return render(request, 'generator/readme.html')
