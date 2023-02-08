from django.shortcuts import render

from django.views.generic import TemplateView

from .models import PersonalInfo


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["info"] = PersonalInfo.objects.get(id=1)

        return context
