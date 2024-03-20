from . import views
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'hoodie', views.HoodiesViewSet)

urlpatterns = [
    path('hoodies/', views.order_hoodies, name='order_hoodies'),
    path('api/', include(router.urls)),
]