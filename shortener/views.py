from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import shorturl

def test_view(request):
    return HttpResponse("some stuff")

def kirr_redirect_view(request, shortcode=None, *args, **kwargs):
    obj = get_object_or_404(shorturl, shortcode=shortcode)
    return HttpResponse("hello {sc}".format(sc=shortcode))

class kirrCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(shorturl, shortcode=shortcode)
        return HttpResponse("hello agins {sc}".format(sc=shortcode))

    def post(self, request, *args, **kwargs):
        return HttpResponse()
