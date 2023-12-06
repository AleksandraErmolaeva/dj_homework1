from django.contrib import admin
from .models import Sensor, Measurement

# Register your models here.
@admin.register(Sensor)
class Sensor(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']

@admin.register(Measurement)
class Measurement(admin.ModelAdmin):
    list_display = ['sensor', 'temperature', 'created_at']