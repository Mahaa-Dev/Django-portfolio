from django.urls import path
from .views import HomePageView, About, ContactCreate, ProjectDetailView, EducationView, TempView

urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
    path("a/", TempView.as_view(), name='temp'),

    path("contact/", ContactCreate.as_view(), name="contact"),

    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail')

]
