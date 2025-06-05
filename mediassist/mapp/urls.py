
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('reg/', views.reg),
    path('login/', views.log),
    path('user/', views.user),
    path('edit/<int:idl>/', views.edit, name='edit'),
    path('delete/<int:idl>/', views.delete, name='delete'), 
    path('medicine/',views.medicine),
    path('medicineview/',views.medicineview),
]
