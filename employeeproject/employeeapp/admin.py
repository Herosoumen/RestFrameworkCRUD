from django.contrib import admin
from .models import Address,Profile
# Register your models here.


class AddressAdmin(admin.ModelAdmin):
    list_display = ['street_no','city','state','pincode','country','created_at','updated_at']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','permanent_address_city','phone_number','gender','created_at','updated_at']


admin.site.register(Address,AddressAdmin)
admin.site.register(Profile,ProfileAdmin)
