from django.urls import path
from . import views;

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('addBuilding/', views.add_building_view, name='addBuilding'),
    path('update/<int:id>/', views.update_building_view, name='updateBuilding'),
    
    #  Tenants
    path('addTenant/', views.add_tenant_view, name='addTenant'),
    path('tenants/', views.tenants_view, name='tenants'),
    path('updatetenant/<int:id>/', views.update_tenant_view, name='updateTenant'),
    
    # Bulding Tenants
    
    path('building_tenants/', views.buildnig_tenants_view, name='btenants'),
    path('add_b_tenants/', views.add_b_tenant, name='addbtenants'),
]
