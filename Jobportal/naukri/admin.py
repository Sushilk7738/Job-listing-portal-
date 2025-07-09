from django.contrib import admin
from naukri.models import Mumbai, Pune, Bengaluru

# Register your models here.

class MumbaiAdmin(admin.ModelAdmin):
    list_display = ["company_name", "job_title", "sal", "qualification", "joining_date", "location" ,"address"]

class PuneAdmin(admin.ModelAdmin):
    list_display = ["company_name", "job_title", "sal", "qualification", "joining_date", "location" ,"address"]

class BengaluruAdmin(admin.ModelAdmin):
    list_display = ["company_name", "job_title", "sal", "qualification", "joining_date", "location" ,"address"]
    

admin.site.register(Mumbai, MumbaiAdmin)
admin.site.register(Pune, PuneAdmin)
admin.site.register(Bengaluru, BengaluruAdmin)