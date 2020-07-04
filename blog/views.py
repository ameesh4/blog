import requests
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import POST

def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')

class PostList(generic.ListView):
    queryset = POST.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = POST
    template_name = 'post_detail.html'


# Create your views here.
