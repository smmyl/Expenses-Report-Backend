from django.urls import path, include
from rest_framework import routers
from .views import NamesList

router = routers.DefaultRouter()
router.register(r'name', NamesList) 

urlpatterns = [
    # ... other urls
    path('api/names', views.NamesList.as_view(), name='names_list'),
    path('api/names/<int:pk>', views.NamesDetail.as_view(), name='names_detail'),
]