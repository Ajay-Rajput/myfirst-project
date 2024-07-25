from django.contrib import admin
from todo_list.models import todo

def mark_task_completed(modeladmin, request, queryset):
    queryset.update(completed=True)
mark_task_completed.short_description='mark selected task completed'

class todoAdmin(admin.ModelAdmin):
    list_display=('title','description','completed')
    actions=[mark_task_completed]

admin.site.register(todo,todoAdmin)

# Register your models here.
