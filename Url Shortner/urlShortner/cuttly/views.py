from django.shortcuts import render
import pyshorteners
import time

def shorten_url(url):
    s = pyshorteners.Shortener(api_key='76ce1df69422cb3cca6a792ad29a2f9ca5f26')
    return s.cuttly.short(url)

def cuttly(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url', '')
        if long_url:
            shortened_url = shorten_url(long_url)
            return render(request, 'cuttly.html', {'shortened_url': shortened_url})
    
    return render(request, 'cuttly.html')
