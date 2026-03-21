from django.db import models
from django.utils import timezone  # This fixes the "not defined" error for timezone 

class BaseModel(models.Model):
    # Inherit BaseModel with created_at and updated_at fields [cite: 65]
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True 

class Priority(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        # Refactor to use grammatically correct plural name [cite: 85, 87]
        verbose_name_plural = "Priorities"

    def __str__(self):
        return self.name #[cite: 94]

class Category(models.Model):
    name = models.CharField(max_length=100)# [cite: 89]

    class Meta:
        # Refactor to use grammatically correct plural name [cite: 85, 92]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name #[cite: 94]

class Task(BaseModel):
    # Field choices (enumeration) for status [cite: 67, 71]
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    status = models.CharField(
        max_length=50, 
        choices=STATUS_CHOICES, 
        default="Pending"
    ) #[cite: 69, 70, 77]
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)

    def __str__(self):
        return self.title #[cite: 66]

class SubTask(BaseModel):
    parent_task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="subtasks")
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=Task.STATUS_CHOICES, default="Pending")

    def __str__(self):
        return self.title #[cite: 66]

class Note(BaseModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="notes")
    content = models.TextField()

    def __str__(self):
        return f"Note for {self.task.title}" #[cite: 66]