from django.urls import path 
import Prediction.views as views

urlpatterns = [
    path('add/', views.api_add, name = "api_add"),
    path('add_values/', views.Add_values.as_view(), name = "api_add_values"),
]
