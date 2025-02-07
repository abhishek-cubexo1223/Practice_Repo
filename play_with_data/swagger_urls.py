from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# ✅ Basic Schema View (Minimum Required)
schema_view = get_schema_view(
    openapi.Info(
        title="This is a dummy demo task",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# ✅ Minimum Required URLs
swagger_urls = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
