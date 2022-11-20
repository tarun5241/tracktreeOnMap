from django.contrib import admin

from ngo.models import Ngo,Event

# Register your models here.

# class ClasssAdmin(admin.ModelAdmin):
#     list_display = ['className','schoolId']

class NgoAdmin(admin.ModelAdmin):
    list_display = ['name','ngo_name','email','total_member','created']
    
class EventAdmin(admin.ModelAdmin):
    list_display = ['ngo_name','event_name','event_date','trees_planted']

# Register your models here.
admin.site.register(Ngo, NgoAdmin)
admin.site.register(Event, EventAdmin)