from django.urls import path, include
from rest_framework import routers
from .views import NameViewSet

router = routers.DefaultRouter()
router.register(r'name', NameViewSet) 

urlpatterns = [
    # ... other urls
    path('api/', include(router.urls)),
]