from django.shortcuts import render

from django.views.generic import TemplateView, CreateView

from .models import PersonalInfo, Contact
from .forms import ContactForm


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["info"] = PersonalInfo.objects.get(id=1)
        context["form"] = ContactForm()

        return context


class About(TemplateView):
    template_name = "about.html"


class ContactCreate(CreateView):
    template_name = "contact_form.html"
    model = Contact
    form_class = ContactForm
    success_url = "/"
