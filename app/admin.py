from django.contrib import admin
from app.models import Project
# Register your models here.
@admin.register(Project)
class ProjectModelAdmin(admin.ModelAdmin):

    list_display = ['project','user']
