"""muypicky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
#from restuarants.views import HomeView,AboutView
from django.views.generic import TemplateView
from restuarants.views import restuarant_list,RestuarantListView,RestuarantDetailView,RestuarantCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$', TemplateView.as_view(template_name = 'home.html')),
    url('^about/$', TemplateView.as_view(template_name = 'about.html')),
    url('^restuarants/$', RestuarantListView.as_view()),
    url('^restuarants/create/$', RestuarantCreateView.as_views()),
    url('^restuarants/(?P<slug>[\w-]+)/$', RestuarantDetailView.as_view()),
    #url('^restuarants/(?P<rest_id>\w+)/$', RestuarantDetailView.as_view()),
    #url('^restuarants/gastropub/$', GastropubListView.as_view()),
    url('^contact/$', TemplateView.as_view(template_name = 'contact.html')),
]
