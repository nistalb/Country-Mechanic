from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('garage/', views.garage, name='garage'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('equipment/create', views.equipment_create, name='equipment_create'),
    path('equipment/<int:equipment_id>/show', views.equipment_show, name='equipment_show'),
    path('equipment/<int:equipment_id>/edit', views.equipment_edit, name='equipment_edit'),
    path('eqiupment/<int:equipment_id>/delete', views.equipment_delete, name='equipment_delete'),
    
]
