from django.shortcuts import render
import pyshorteners
import time

def shorten_url(url):
    s = pyshorteners.Shortener(api_key='5789cb55e916f992f8c406e35cb773ea40d621c0')
    return s.bitly.short(url)

def bitly(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url', '')
        if long_url:
            shortened_url = shorten_url(long_url)
            return render(request, 'bitly.html', {'shortened_url': shortened_url})
    
    return render(request, 'bitly.html')

