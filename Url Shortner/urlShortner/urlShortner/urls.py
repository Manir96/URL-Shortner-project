from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('bitly/', include('bitly.urls')),
    path('cuttly/', include('cuttly.urls')),
    path('rebrandly/', include('rebrandly.urls')),
    path('tiniurl/', include('tiniurl.urls')),
]
