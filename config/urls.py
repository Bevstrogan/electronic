from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from providers.views import ProviderViewSet
from users.views import UserViewSet

router = DefaultRouter()
router.register(r'providers', ProviderViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
]
