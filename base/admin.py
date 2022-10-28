from django.contrib import admin
from .models import Doctor, Patient, Consultations
# Register your models here.

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Consultations)