from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse,HttpResponseRedirect
import random
from django.views import View
from django.views.generic import TemplateView, ListView,DetailView,CreateView,UpdateView
from .models import RestuarantLocation
from .forms import RestuarantCreateForm,RestuarantLocationCreateForm


# Create your views here.

class RestuarantListView(LoginRequiredMixin,ListView):
    template_name = 'restuarants/restuarants_list.html'
    def get_queryset(self):
        return RestuarantLocation.objects.filter(owner = self.request.user)

class RestuarantDetailView(LoginRequiredMixin,DetailView):
    def get_queryset(self):
        return RestuarantLocation.objects.filter(owner = self.request.user)

    # def get_object(self, queryset=None):
    #     rest_id = self.kwargs.get('rest_id')
    #     obj = get_object_or_404(RestuarantLocation,id = rest_id) #pk = rest_id
    #     return obj

class RestuarantCreateView(LoginRequiredMixin,CreateView):
    form_class = RestuarantLocationCreateForm
    login_url = '/login/'
    template_name = 'form.html'
    #success_url = '/restuarants/'

    def form_valid(self, form):
        instance = form.save(commit = False)
        instance.owner = self.request.user
        instance.save()
        return super(RestuarantCreateView,self).form_valid(form)

    def get_context_data(self, **kwargs):
        context =  super(RestuarantCreateView,self).get_context_data(**kwargs)
        context['title'] = 'Add Restuarant'
        return context

class RestuarantUpdateView(LoginRequiredMixin,UpdateView):
    form_class = RestuarantLocationCreateForm
    login_url = '/login/'
    template_name = 'restuarants/detail-update.html'
    #success_url = '/restuarants/'

    def get_context_data(self, **kwargs):
        context =  super(RestuarantUpdateView,self).get_context_data(**kwargs)
        name = self.get_object().name
        context['title'] = f'Update Restuarant : {name}'
        return context

    def get_queryset(self):
        return RestuarantLocation.objects.filter(owner = self.request.user)