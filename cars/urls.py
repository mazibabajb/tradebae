from django.urls import path
from.import views
from .views import CarListView,CarDetailView


urlpatterns = [
    path('', views.home, name ='home'),
    path('car',CarListView.as_view(), name ='car'),
    path('car/<int:pk>/',CarDetailView.as_view(), name ='car_detail'),
    path('contact_us', views.contact_us, name ='contact_us'),
    path('about_us', views.about_us, name ='about_us'),

]
