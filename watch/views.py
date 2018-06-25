from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    title = 'Hood-Watch'

    return render(request, 'index.html',{'title':title})