from django.contrib import admin
from django.forms.widgets import TextInput

from django_google_maps.widgets import GoogleMapsAddressWidget
from django_google_maps.fields import AddressField, GeoLocationField

from .models import Profile

# Register your models here.
admin.site.register(Profile)


class HoodCustom(admin.ModelAdmin):
    formfield_overrides = {
        AddressField:{
            'widget': GoogleMapsAddressWidget
        },
        GeoLocationField:{
            'widget': TextInput(attrs={
                'readonly':'readonly'
            })
        }
    }

admin.site.register(Hood, HoodCustom)