from django.conf.urls import url

from .views import ItemListView,ItemDetailView,ItemCreateView,ItemUpdateView

urlpatterns = [
    url('^create$', ItemCreateView.as_view(),name = 'create'),
    #url('^(?P<pk>\d+)/edit$', ItemUpdateView.as_view(),name = 'edit'),
    url('^(?P<pk>\d+)/$', ItemUpdateView.as_view(),name = 'detail'),
    url('$', ItemListView.as_view(),name = 'list'),
]
