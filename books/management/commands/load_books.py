# books/management/commands/load_books.py

import csv
from django.core.management.base import BaseCommand
from books.models import Book

class Command(BaseCommand):
    help = 'Load books data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Book.objects.create(
                    name=row['name'],
                    author=row['author'],
                    genre=row['genre'],
                    published_year=row['published_year'],
                    description=row['description']
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from CSV file'))
