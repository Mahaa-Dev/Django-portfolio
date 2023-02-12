from django.shortcuts import render

from django.views.generic import TemplateView, CreateView, DetailView, ListView

from .models import PersonalInfo, Contact, About, Project, Education, CurrentJob
from .forms import ContactForm


# Create your views here.
class TempView(TemplateView):
    template_name = 'a.html'


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["info"] = PersonalInfo.objects.get(id=1)
        context["about"] = About.objects.last()
        context["form"] = ContactForm()
        context["posts"] = Project.objects.all()

        context["learning"] = Education.objects.all()
        context['current_jobs'] = CurrentJob.objects.all()

        return context


# class About(TemplateView):
#     template_name = "about.html"


class ContactCreate(CreateView):
    template_name = "contact_form.html"
    model = Contact
    form_class = ContactForm
    success_url = "/"


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_view.html'
    context_object_name = 'post'


class EducationView(ListView):
    model = Education
    template_name = 'index.html'
    context_object_name = 'education'
