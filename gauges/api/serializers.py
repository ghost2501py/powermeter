from rest_framework import serializers

from ..models import Gauge, Measurement


class GaugeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gauge
        fields = ['key', 'name']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['kwh', 'registered_at']
