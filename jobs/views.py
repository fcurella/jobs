from django.shortcuts import get_object_or_404
from django.views import generic
from jobs.models import Application


class ApplicationDetailView(generic.DetailView):
    def get_object(self):
        return get_object_or_404(Application, key=self.kwargs.get('key'))
