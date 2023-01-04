from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.

from .models import Project, Actu, About

admin.site.register(Project)
admin.site.register(Actu)
admin.site.register(About)