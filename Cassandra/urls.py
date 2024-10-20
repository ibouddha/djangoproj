from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name="accueil"),
    path('create/', views.create, name="create"),
    path('update/<uuid:id>/', views.update, name="update"),
    path('delete/<uuid:id>/', views.delete, name="delete"),
]
