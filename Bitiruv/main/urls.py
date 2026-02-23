from django.urls import path
from . import views

urlpatterns = [
    path('', views.access_login, name='access_login'),
    path('home/', views.home, name='home'),
    path('graduate/<int:pk>/', views.graduate_detail, name='graduate_detail'),
]