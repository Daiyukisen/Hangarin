from django.contrib import admin
from .models import Priority, Category, Task, SubTask, Note

# This lets you manage SubTasks inside the Task editor
class SubTaskInline(admin.TabularInline):
    model = SubTask
    extra = 1
    fields = ('title', 'status')

class NoteInline(admin.TabularInline):
    model = Note
    extra = 1
    fields = ('content',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'deadline', 'priority', 'category', 'created_at')
    list_filter = ('status', 'priority', 'category', 'created_at')
    search_fields = ('title', 'description')
    
    inlines = [SubTaskInline, NoteInline]

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'parent_task')
    list_filter = ('status',)
    search_fields = ('title',)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('task', 'content_snippet', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('content',)

    @admin.display(description='Content')
    def content_snippet(self, obj):
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)