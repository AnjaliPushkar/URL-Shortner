from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from shortener.views import HomeView, kirrCBView

urlpatterns = [
    url(r'(?P<shortcode>[\w-]+){6,15}/$', kirrCBView.as_view()),
    path('admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    path('', include('shortener.urls')),
]
