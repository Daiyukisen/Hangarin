import os
import django
import random
from faker import Faker
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hangarin.settings')
django.setup()

from tasks.models import Task, SubTask, Note, Category, Priority

fake = Faker()

def populate(n=10):
    categories = list(Category.objects.all())
    priorities = list(Priority.objects.all())

    if not categories or not priorities:
        print("Error: Please add Categories and Priorities in the Admin panel first!")
        return

    status_options = ["Pending", "In Progress", "Completed"]

    for _ in range(n):
        task = Task.objects.create(
            title=fake.sentence(nb_words=5),
            description=fake.paragraph(nb_sentences=3),
            deadline=timezone.make_aware(fake.date_time_this_month()),
            status=fake.random_element(elements=status_options),
            category=random.choice(categories),
            priority=random.choice(priorities)
        )

        for _ in range(2):
            SubTask.objects.create(
                parent_task=task,
                title=fake.sentence(nb_words=3),
                status=fake.random_element(elements=status_options)
            )

        Note.objects.create(
            task=task,
            content=fake.paragraph(nb_sentences=2)
        )

    print(f"Successfully populated the database with {n} Tasks, their SubTasks, and Notes.")

if __name__ == '__main__':
    populate(10)