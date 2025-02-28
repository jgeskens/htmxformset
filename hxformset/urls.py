from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='hxformset_index'),
]
