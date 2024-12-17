from django.urls import path
from .import views


urlpatterns = [
   path('api/nam', views.NameList.as_view(), name='name_list'),
   path('api/name/<int:pk>', views.nameDetail.as_view(), name='name_detail'),
]
