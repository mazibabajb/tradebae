from django.urls import path
from.import views

urlpatterns = [
    path('accessories', views.accessories, name ='accessories'),
    path('accessori_detail', views.accessori_detail, name ='accssori_detail'),
]
