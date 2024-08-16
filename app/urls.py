from django.urls import path
from app import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('read/', views.read),
    path('delete/<int:id>/', views.delete),
    path('create/', views.create),
    path('update/<int:id>/', views.update),
    path('login/', views.loginn),
    path('register/', views.registerr),

]