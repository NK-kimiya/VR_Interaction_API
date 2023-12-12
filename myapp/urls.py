from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
     path('api/custom-model/', views.CustomModelListCreateView.as_view(), name='custommodel-list-create'),
     path('api/check-id/', views.get_entry_by_id, name='check-id-byid'),
     path('api/get-name-and-id/', views.get_name_and_id_by_password, name='get-name-and-id-by-password'),
     path("test", views.IndexView.as_view(), name="index"),
]
