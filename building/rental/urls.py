from django.urls import path
from . import views;

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('addBuilding/', views.add_building_view, name='addBuilding'),
    path('update/<int:id>/', views.update_building_view, name='updateBuilding')
]
