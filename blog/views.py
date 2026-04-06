from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi There! You are at the main site index.")

def about(request):
    return HttpResponse("Hi There! You are viewing the 'about me' page.")

def contact(request):
    return HttpResponse("Hi There! You are viewing the contact page.")

def entry(request):
    return HttpResponse("Hi There! You are viewing the entry page.")

def entry_detail(request, entry_id):
    return HttpResponse("Hi There! You are viewing the entry detail page.")