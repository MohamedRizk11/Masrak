from django.contrib import admin
from .models import Station,Ticket,Roads,Users,FamousPlace

class famousplaces(admin.TabularInline):
    model = FamousPlace

class stationplace(admin.ModelAdmin):
    inlines=[famousplaces] 

class famousplace(admin.ModelAdmin):
    list_display=['name','id','station'] 

# Register your models here.
admin.site.register(Station,stationplace)
admin.site.register(Ticket)
admin.site.register(Roads)
admin.site.register(Users)
admin.site.register(FamousPlace,famousplace)