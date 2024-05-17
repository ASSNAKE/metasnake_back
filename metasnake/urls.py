from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from django.conf import settings
from rest_framework import permissions

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Metasnake API",
        default_version="v1",
        description="Some description",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('api/user/', include('metasnake.apps.users.urls')),
    path('api/data/', include('metasnake.apps.data.urls')),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]