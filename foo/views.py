from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from foo.models import Bar


class BarCreateView(CreateView):
    model = Bar

    def get_success_url(self):
        return '/'


class BarListView(ListView):
    model = Bar
