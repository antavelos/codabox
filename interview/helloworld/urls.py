from django.conf.urls import url

from . import views

app_name = 'helloworld'

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
