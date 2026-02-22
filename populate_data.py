import os
import django
import random
from faker import Faker
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hangarin.settings')
django.setup()

from tasks.models import Task, SubTask, Note, Category, Priority

fake = Faker()

def populate(n=100):
    # Fetch the manual records we created earlier
    categories = list(Category.objects.all())
    priorities = list(Priority.objects.all())

    if not categories or not priorities:
        print("Error: Please add Categories and Priorities in the Admin panel first!")
        return

    print(f"Generating {n} tasks with related notes and subtasks...")

    for _ in range(n):
        
        task = Task.objects.create(
            title=fake.sentence(nb_words=5),
            description=fake.paragraph(nb_sentences=3),
            deadline=timezone.make_aware(fake.date_time_this_month()),
            status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
            category=random.choice(categories),
            priority=random.choice(priorities)
        )

        SubTask.objects.create(
            parent_task=task,
            title=fake.sentence(nb_words=3),
            status=fake.random_element(elements=["Pending", "In Progress", "Completed"])
        )

        Note.objects.create(
            task=task,
            content=fake.paragraph(nb_sentences=2)
        )

    print(f"Success: Created {n} Task, Note, and SubTask records.")

if __name__ == '__main__':
    populate(100)