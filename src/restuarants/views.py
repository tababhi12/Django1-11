from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
import random
from django.views import View
from django.views.generic import TemplateView, ListView
from .models import RestuarantLocation


# Create your views here.

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



