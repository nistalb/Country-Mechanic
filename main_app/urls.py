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
    path('task/<int:equipment_id>/create', views.task_create, name='task_create'),
    path('task/<int:task_id>/show', views.task_show, name='task_show'),
    path('task/<int:task_id>/edit', views.task_edit, name='task_edit'),
    path('task/<int:task_id>/delete', views.task_delete, name='task_delete'),
    path('task/<int:task_id>/assoc_tool/<int:tool_id>', views.tool_assoc, name='tool_assoc'),
    path('task/<int:task_id>/deassoc_tool/<int:tool_id>', views.tool_deassoc, name='tool_deassoc'),
    path('record/<int:equipment_id>/<int:task_id>', views.create_maint_record, name='create_maint_record'),
    path('tool/index', views.tool_index, name='tool_index'),
    path('tool/create', views.tool_create, name='tool_create'),
    path('tool/<int:tool_id>/delete', views.tool_delete, name='tool_delete'),
    path('consumable/index', views.consumable_index, name='consumable_index'),
    path('consumable/create', views.consumable_create, name='consumable_create'),
    path('consumable/<int:consumable_id>/delete', views.consumable_delete, name='consumable_delete'),
    path('task/<int:task_id>/assoc_consumable/<int:consumable_id>', views.consumable_assoc, name='consumable_assoc'),
    path('task/<int:task_id>/deassoc_consumable/<int:consumable_id>', views.consumable_deassoc, name='consumable_deassoc'),    
    
]
