from django.contrib import admin

from . import models


@admin.register(models.TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ['created', 'description', 'done']
    readonly_fields = ['created']
