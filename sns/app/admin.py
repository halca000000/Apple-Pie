# app/admin.py

from django.contrib import admin
from .models import Post, Comment
from django.contrib.admin.models import LogEntry

class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'action_time', 'object_id', 'object_repr', 'action_flag', 'change_message')

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(LogEntry, LogEntryAdmin)
