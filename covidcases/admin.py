from django.contrib import admin

from .models import Country,Patients,User
# Register your models here.
admin.site.register(Country)
admin.site.register(Patients)
admin.site.register(User)
