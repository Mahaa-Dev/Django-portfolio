from django.contrib import admin

# Register your models here.

from .models import PersonalInfo, Contact, About, Project

admin.site.register([
    PersonalInfo,
    Contact,
    About,
    Project
])
