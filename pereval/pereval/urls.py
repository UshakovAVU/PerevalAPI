from django.contrib import admin
from django.urls import path
from mountpass import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/submitdata/', views.PerevalViewset.as_view({'post': 'create', 'get': 'list'})),
    path('api/submitdata/<int:pk>/', views.PerevalViewset.as_view({'get': 'retrieve', 'patch': 'partial_update'})),
]
