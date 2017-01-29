from django.views import generic

from .models import Entity


class DetailView(generic.DetailView):
    model = Entity
    template_name = 'helloworld/detail.html'
