from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

def kirr_redirect_view(request):
    return HttpResponse("hello")

class kirrCBView(View):
    def get(self, request):
        return HttpResponse("hello agins")
