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
from django.urls import path,include
from django.conf.urls import url,include
from django.contrib.auth.views import LoginView
#from restuarants.views import HomeView,AboutView
from django.views.generic import TemplateView
from restuarants.views import restuarant_list,RestuarantListView,RestuarantDetailView,RestuarantCreateView,restuarant_createview

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$', TemplateView.as_view(template_name = 'home.html'),name = 'home'),
    url('^about/$', TemplateView.as_view(template_name = 'about.html'),name = 'about'),
    url('^login/$', LoginView.as_view(),name = 'login'),
    url('^items/', include(('menus.urls','menus'),namespace = 'menus')),
    url('^restuarants/', include(('restuarants.urls','restuarants'),namespace = 'restuarants')),
    url('^contact/$', TemplateView.as_view(template_name = 'contact.html'),name = 'contact'),
]
