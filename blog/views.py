# from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

# def home(request):
#     if request.method == 'POST':
#         return HttpResponse('Hi')
#     elif request.method == 'GET':
#         return HttpResponse('Good')

from . import models


class HomeView(View):
    '''Home page'''

    def get(self, request):
        posts = models.Post.objects.all()
        return render(request, 'blog/home.html', {'posts': posts})


class PostView(View):
    '''Вывод статей категории'''


    def get(self, request, post_name):
        post = models.Post.objects.get(slug=post_name)
        return render(request, 'blog/post_list.html', {'information': post})
