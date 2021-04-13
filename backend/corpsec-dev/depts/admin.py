from django.contrib import admin
from .models import Department
from mptt.admin import DraggableMPTTAdmin

class DepartmentAdmin(DraggableMPTTAdmin):
    pass

admin.site.register(Department, DepartmentAdmin )