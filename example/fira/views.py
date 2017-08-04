from django.views.generic import CreateView
from fira.models import Fira
from fira.forms import FiraForm


class FiraCreateView(CreateView):
    model = Fira
    form_class = FiraForm
    template_name = 'create.html'
    success_url = '/'
