from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers, permissions
from mountpass import views
from django.conf import settings
from django.conf.urls.static import static

# Создаем роутер для ViewSet
router = routers.DefaultRouter()
router.register(r'api/submitdata', views.PerevalViewSet, basename='pereval')

# Настройка Swagger Schema
schema_view = get_schema_view(
    info=openapi.Info(
        title="Pereval API",
        default_version='v1',
        description="API для работы с данными о перевалах",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@yourcompany.com"),
        license=openapi.License(name="BSD License"),
    ),
    validators=['flex'],
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # URL для Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # URL для ReDoc
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # OpenAPI JSON/YAML
    path('openapi/', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    # API endpoints
    path('', include(router.urls)),

    # Дополнительные URL, если необходимо
    # path('api/other-endpoint/', views.OtherView.as_view(), name='other-endpoint'),
]

# Обработка статических файлов для режима разработки
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
