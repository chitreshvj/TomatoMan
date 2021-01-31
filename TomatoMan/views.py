from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

def index_page (request) :
    return HttpResponse("Welcome to my TomatoMan")