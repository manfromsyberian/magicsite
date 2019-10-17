from django.conf.urls import url

from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path(r'catalog/plants', views.plants, name='plants'),
    path(r'catalog/liquids', views.liquids, name='liquids'),
    path(r'catalog/items', views.items, name='items'),
    path(r'contacts', views.contacts, name='contacts'),
    path('payment', views.payment, name='payment'),
]
