from rest_framework_extensions.routers import ExtendedSimpleRouter

from .views import GaugeViewSet, MeasurementViewSet

router = ExtendedSimpleRouter()
(
    router.register(r'gauges', GaugeViewSet, basename='gauges')
        .register(
            r'measurements',
            MeasurementViewSet,
            basename='measurements',
            parents_query_lookups=['gauge'],
        )
)
