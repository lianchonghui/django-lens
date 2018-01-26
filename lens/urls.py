from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^all/',views.AllView.as_view(),name='all'),
    url(r'^lens/',views.lens,name='lens'),
    url(r'^drop/',views.droploadindex,name='drop'),
    url(r'^$',views.IndexView.as_view(),name='index'),
]