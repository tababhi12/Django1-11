from django.shortcuts import render
from django.http import HttpResponse
import random
from django.views import View
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'
    #context = super(HomeView, self).get_context_Data(*args,**kwargs)
    def get_context_data(self,*args,**kwargs):
        some_list = [
            random.randint(0, 10000),
            random.randint(0, 10000),
            random.randint(0, 10000)
        ]
        conditional_bool_item = True
        if conditional_bool_item:
            num = random.randint(0, 10000)
        context = {'html_var': 'HTML', 'num': num, 'some_list': some_list}
        return context


class AboutView(TemplateView):
    template_name = 'about.html'



