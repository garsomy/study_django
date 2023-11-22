from django.shortcuts import render
from django.http import HttpResponse

def index(request, name, age, interests):
    return HttpResponse(f'Me: <br> My name is {name} <br> I am {age} years old. <br> My interests {interests}')


def about(request, city, functionality, study):
    return HttpResponse(f'I am from {city}, my functionality is {functionality}, and study {study}')


def contact(request, github, phone):
    return HttpResponse(f'My Github: {github}, other contacts: {phone}')