from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from orderapp import views


router = routers.DefaultRouter()
router.register(r'orders', views.OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]