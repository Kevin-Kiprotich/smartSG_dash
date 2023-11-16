from django.contrib import admin
from .models import Rider, Offence

class OffenceAdmin(admin.ModelAdmin):
    list_display = ('time', 'rider_first_name', 'rider_last_name', 'rider_number_plate','rider_offence_count',)

    def rider_first_name(self, obj):
        return obj.vehicle.first_name

    def rider_last_name(self, obj):
        return obj.vehicle.last_name

    def rider_number_plate(self, obj):
        return obj.vehicle.number_plate
    
    def rider_offence_count(self,obj):
        return obj.vehicle.offence_count

    rider_first_name.short_description = 'Rider First Name'
    rider_last_name.short_description = 'Rider Last Name'
    rider_number_plate.short_description = 'Rider Number Plate'
    rider_offence_count.short_description='Offence Count'
class RiderAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','ID_Number','brand','model','number_plate','offence_count',)

admin.site.register(Rider,RiderAdmin)
admin.site.register(Offence, OffenceAdmin)