from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url,include
from django.contrib.auth.views import LoginView
#from restuarants.views import HomeView,AboutView
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$', TemplateView.as_view(template_name = 'home.html'),name = 'home'),
    url('^about/$', TemplateView.as_view(template_name = 'about.html'),name = 'about'),
    url('^login/$', LoginView.as_view(),name = 'login'),
    url(r'^u/', include(('profiles.urls','profiles'),namespace = 'profile')),
    url('^items/', include(('menus.urls','menus'),namespace = 'menus')),
    url('^restuarants/', include(('restuarants.urls','restuarants'),namespace = 'restuarants')),
    url('^contact/$', TemplateView.as_view(template_name = 'contact.html'),name = 'contact'),
]
