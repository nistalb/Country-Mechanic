from django.contrib import admin
from .models import Profile, Equipment, Task, Tool, Consumables, Maint_Record

# Register your models here.

admin.site.register(Profile)
admin.site.register(Equipment)
admin.site.register(Task)
admin.site.register(Tool)
admin.site.register(Consumables)
admin.site.register(Maint_Record)
