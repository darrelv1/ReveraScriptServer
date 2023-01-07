from django.urls import path
from . import views

urlpatterns = [
    path('accountant/', views.index) #Don't pass with parenthesis : view.index
]