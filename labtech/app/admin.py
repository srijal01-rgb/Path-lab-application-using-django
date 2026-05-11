from django.contrib import admin
from .models import Patient, Test, LabReport

class PatientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'date_of_birth')

class TestAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')

class LabReportAdmin(admin.ModelAdmin):
    list_display = ('patient', 'test', 'result', 'date_conducted')

admin.site.register(Patient, PatientAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(LabReport, LabReportAdmin)
# modelAdmin
# Admin panel मा column हरू देखिन्छ
# Data खोज्न सजिलो हुन्छ
# Professional look आउँछ