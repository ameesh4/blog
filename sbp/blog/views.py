from django.shortcuts import render
from django.views import generic

from .models import POST

class PostList(generic.ListView):
    queryset = POST.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = POST
    template_name = 'post_detail.html'


# Create your views here.
