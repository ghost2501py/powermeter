from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework_extensions.utils import compose_parent_pk_kwarg_name

from .serializers import GaugeSerializer, MeasurementSerializer
from ..models import Gauge, Measurement


class GaugeViewSet(
        NestedViewSetMixin,
        mixins.CreateModelMixin,
        viewsets.GenericViewSet):
    queryset = Gauge.objects.all()
    serializer_class = GaugeSerializer

    @action(methods=['get'], detail=True, url_path='max-consumption', url_name='max_consumption')
    def max_consumption(self, *args, **kwargs):
        obj = self.get_object()
        return Response({'max_consumption': obj.max_consumption}, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True, url_path='min-consumption', url_name='min_consumption')
    def min_consumption(self, *args, **kwargs):
        obj = self.get_object()
        return Response({'min_consumption': obj.min_consumption}, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True, url_path='total-consumption', url_name='total_consumption')
    def total_consumption(self, *args, **kwargs):
        obj = self.get_object()
        return Response({'total_consumption': obj.total_consumption}, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True, url_path='average-consumption', url_name='average_consumption')
    def average_consumption(self, *args, **kwargs):
        obj = self.get_object()
        return Response({'average_consumption': obj.average_consumption}, status=status.HTTP_200_OK)


class MeasurementViewSet(
        NestedViewSetMixin,
        mixins.CreateModelMixin,
        viewsets.GenericViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def perform_create(self, serializer):
        gauge_pk = self.kwargs[compose_parent_pk_kwarg_name('gauge')]
        serializer.save(gauge_id=gauge_pk)
