from django.contrib import admin

# Register your models here.

from .models import PersonalInfo, Contact, About, Project, Education, CurrentJob

admin.site.register([
    PersonalInfo,
    Contact,
    About,
    Project,
    Education,
    CurrentJob
])
