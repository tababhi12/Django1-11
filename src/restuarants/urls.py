from django.conf.urls import url

from .views import RestuarantListView,RestuarantDetailView,RestuarantCreateView,RestuarantUpdateView

urlpatterns = [
    url('^create/$', RestuarantCreateView.as_view(),name = 'create'),
    #url('^(?P<slug>[\w-]+)/edit/$', RestuarantUpdateView.as_view(),name = 'edit'),
    url('^(?P<slug>[\w-]+)/$', RestuarantUpdateView.as_view(),name = 'detail'),
    url('$', RestuarantListView.as_view(),name = 'list'),
]
