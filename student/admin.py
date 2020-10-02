from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Address', {'fields': ['address']}),
    ]
    list_display = ['name', 'address', 'created_at']

admin.site.register(Student, StudentAdmin)
