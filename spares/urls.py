from django.urls import path
from.import views

urlpatterns = [
    path('spares', views.spares, name ='spares'),
    path('spare_detail', views.spare_detail, name ='spare_detail'),
]
