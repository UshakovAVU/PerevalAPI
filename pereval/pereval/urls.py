
from django.contrib import admin
from django.urls import path, include
from mountpass import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'pereval', views.PerevalViewset, basename='pereval')
router.register(r'user', views.UserViewset, basename='user')
router.register(r'coords', views.CoordsViewset, basename='coords')
router.register(r'level', views.LevelViewset, basename='level')
router.register(r'image', views.ImageViewset, basename='image')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
