from django.db import models
from django.db.models import Avg, Max, Min, Sum
from django.utils.translation import gettext_lazy as _


class Gauge(models.Model):
    key = models.CharField(_('Identification key'), max_length=100, primary_key=True)
    name = models.CharField(_('Name'), max_length=100)

    def __str__(self):
        return self.name

    @property
    def max_consumption(self):
        return self.measurement_set.aggregate(Max('kwh'))['kwh__max'] or 0

    @property
    def min_consumption(self):
        return self.measurement_set.aggregate(Min('kwh'))['kwh__min'] or 0

    @property
    def total_consumption(self):
        return self.measurement_set.aggregate(Sum('kwh'))['kwh__sum'] or 0

    @property
    def average_consumption(self):
        return self.measurement_set.aggregate(Avg('kwh'))['kwh__avg'] or 0


class Measurement(models.Model):
    kwh = models.PositiveIntegerField(_('kWh'))
    registered_at = models.DateTimeField(_('Registered at'))

    gauge = models.ForeignKey(
        Gauge, on_delete=models.SET_NULL, null=True, verbose_name=_('Gauge'))

    def __str__(self):
        return f'{self.gauge.name} {self.registered_at}'
