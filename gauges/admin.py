from django.contrib import admin

from .models import Gauge, Measurement


class MeasurementInline(admin.TabularInline):
    model = Measurement
    extra = 0


@admin.register(Gauge)
class GaugeAdmin(admin.ModelAdmin):
    inlines = [MeasurementInline]
