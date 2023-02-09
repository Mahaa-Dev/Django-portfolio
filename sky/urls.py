from django.urls import path
from .views import HomePageView, About, ContactCreate

urlpatterns = [
    path("", HomePageView.as_view(), name='Home'),
    path("about/", About.as_view(), name='about'),
    path("contact/", ContactCreate.as_view(), name="contact")
]
