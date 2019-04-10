from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from django.http import HttpResponse,HttpResponseRedirect
import random
from django.views import View
from django.views.generic import TemplateView, ListView,DetailView
from .models import RestuarantLocation
from .forms import RestuarantCreateForm


# Create your views here.

def restuarant_createview(request):
    # print(request.GET)
    # if request.method == 'GET':
    #     print('GET DATA')
    form = RestuarantCreateForm()
    if request.method == 'POST':
        # print('POST DATA')
        # title = request.POST.get('title')
        # location = request.POST.get('location')
        # category = request.POST.get('category')
        form = RestuarantCreateForm(request.POST)
        if form.is_valid():
            obj = RestuarantLocation.objects.create(
                name = form.cleaned_data.get('name'),
                location = form.cleaned_data.get('location'),
                category = form.cleaned_data.get('category')
            )
            return HttpResponseRedirect('/restuarants/')
        if form.errors:
            print(form.errors)
    return render(request, template_name='restuarants/form.html', context={'forms':form})

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


