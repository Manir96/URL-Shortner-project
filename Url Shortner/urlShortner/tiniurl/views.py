from django.shortcuts import render
import pyshorteners
import time

def shorten_url(url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)

def tiniurl(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url', '')
        if long_url:
            shortened_url = shorten_url(long_url)
            return render(request, 'tiniurl.html', {'shortened_url': shortened_url})
    
    return render(request, 'tiniurl.html')
