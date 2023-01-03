from rest_framework.schemas import get_schema_view

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from gauges.api.router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    path('api/openapi/', get_schema_view(
        title='Powermeter API',
        description='Powermeter API',
        version='1.0.0'
    ), name='openapi-schema'),
    path('api/docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]
