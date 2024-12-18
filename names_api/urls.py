from django.urls import path
from . import views

urlpatterns = [
    path('names/', views.NamesList.as_view(),name='names-list'),
    path('names/<int:pk>', views.NamesDetail.as_view(), name='names_detail'),
]