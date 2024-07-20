from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ImageViewSet
from . import views
router = DefaultRouter()
router.register(r'images', ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('upload/', views.ImageUploadView.as_view(), name='image-upload'),
]
