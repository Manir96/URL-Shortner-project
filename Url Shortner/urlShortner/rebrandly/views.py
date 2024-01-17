from django.shortcuts import render
import requests

def shorten_url(url):
    api_key = '1059e0f875fb4d84a234f428fece3813'
    api_url = 'https://api.rebrandly.com/v1/links'
    headers = {
        'Content-Type': 'application/json',
        'apikey': api_key
    }
    payload = {
        'destination': url
    }
    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code == 200:
        shortened_url = response.json()['shortUrl']
        return shortened_url
    else:
        return None

def rebrandly(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url', '')
        if long_url:
            shortened_url = shorten_url(long_url)
            if shortened_url:
                return render(request, 'rebrandly.html', {'shortened_url': shortened_url})
            else:
                return render(request, 'rebrandly.html', {'error_message': 'Failed to shorten URL. Please try again.'})
    
    return render(request, 'rebrandly.html')
