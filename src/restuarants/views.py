from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse,HttpResponseRedirect
import random
from django.views import View
from django.views.generic import TemplateView, ListView,DetailView,CreateView
from .models import RestuarantLocation
from .forms import RestuarantCreateForm,RestuarantLocationCreateForm


# Create your views here.
@login_required(login_url='/login/')
def restuarant_createview(request):
    form = RestuarantLocationCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        if request.user.is_authenticated():
            instance = form.save(commit = False)
            instance.owner = request.user
            instance.save()
            return HttpResponseRedirect('/restuarants/')
        else:
            return HttpResponseRedirect('/restuarants/')
    if form.errors:
        errors = form.errors
    return render(request, template_name='restuarants/form.html', context={'form':form,'errors':errors})

def restuarant_list(request):
    queryset = RestuarantLocation.objects.all()
    return render(request, template_name='restuarants/restuarants_list.html', context={'object_list': queryset})


class RestuarantListView(ListView):
    template_name = 'restuarants/restuarants_list.html'
    def get_queryset(self):
        print(self.kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestuarantLocation.objects.filter(Q(category__icontains=slug)| Q(category__iexact=slug))
        else:
            queryset = RestuarantLocation.objects.all()
        return queryset

class RestuarantDetailView(DetailView):
    queryset = RestuarantLocation.objects.all()#filter(category__iexact = 'gastropub')

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
