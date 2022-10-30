from django.contrib import admin
from .models import Doctor, Patient, Consultations
from base.forms import ClientFormAdmin
# Register your models here.

class PatientAdmin(admin.ModelAdmin):
  form = ClientFormAdmin

  class Media:
    js=("jquery.mask.min.js",
         "custom.js",
    )

admin.site.register(Doctor)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Consultations)