from django.contrib import admin
from django.urls import path
from mountpass import views
from .yasg import urlpatterns as doc_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/submitdata/', views.PerevalViewSet.as_view({'post': 'create', 'get': 'list'}), name='pereval-list'),
    path('api/submitdata/<int:pk>/', views.PerevalViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update'}),
                                                                    name='pereval-detail'),
]
urlpatterns += doc_url