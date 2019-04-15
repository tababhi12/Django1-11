from django.conf.urls import url

from .views import RestuarantListView,RestuarantDetailView,RestuarantCreateView

urlpatterns = [
    url('^create/$', RestuarantCreateView.as_view(),name = 'create'),
    url('^(?P<slug>[\w-]+)/$', RestuarantDetailView.as_view(),name = 'detail'),
    url('$', RestuarantListView.as_view(),name = 'list'),
]
