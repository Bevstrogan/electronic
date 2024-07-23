from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from providers.views import ProviderViewSet
from users.views import UserViewSet, ObtainTokenView

router = DefaultRouter()
router.register(r"providers", ProviderViewSet)
router.register(r"users", UserViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path('auth/token/', ObtainTokenView.as_view(), name='obtain_token')
]
