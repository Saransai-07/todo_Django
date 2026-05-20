from django.contrib import admin
from .models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'is_completed', 'created_at', 'updated_at')
    search_fields = ('tasks',)
    list_filter = ('is_completed',)
admin.site.register(Task, TaskAdmin)