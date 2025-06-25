from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# Schema view config
schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="API documentation for your project",
        terms_of_service="https://yourdomain.com/terms/",
        contact=openapi.Contact(email="contact@yourdomain.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Local apps
LOCAL_APPS_URLS = [
    path("banner/", include("apps.banner.urls")),
    path("order/", include("apps.order.urls")),
    path("news/", include("apps.news.urls")),
    path("category/", include("apps.category.urls")),
    path("product/", include("apps.product.urls")),
    path("user/", include("apps.user.urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    *LOCAL_APPS_URLS,

    # Swagger endpoints
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)