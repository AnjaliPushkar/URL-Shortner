
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from shortener.views import kirr_redirect_view, kirrCBView, test_view

urlpatterns = [
    url(r'^a/(?P<shortcode>[\w-]+){6, 15}/$', kirr_redirect_view),
    url(r'^b/(?P<shortcode>[\w-]+){6,15}/$', kirrCBView.as_view()),
    path('admin/', admin.site.urls),
    url(r'^about123/$', test_view),
]
