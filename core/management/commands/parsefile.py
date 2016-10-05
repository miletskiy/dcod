
from django.core.management.base import BaseCommand, CommandError
import os
import csv
from django.conf import settings
from core.models import CitiesData


class Command(BaseCommand):
    """
    Command for parsing CSV file and save the data into DB
    """
    help = """Command for parsing CSV file and save the data into DB.
            arg == filename"""

    def add_arguments(self, parser):
        parser.add_argument('file_name', nargs='+', type=str)

    def handle(self, *args, **options):
        file_extension = options['file_name'][0].split('.')[-1]
        if file_extension != 'csv':
            raise CommandError('Please specify only files in CSV format')
        else:
            file_path = os.path.join(
                settings.MEDIA_ROOT, options['file_name'][0])

            with open(file_path, mode='r') as FILE:
                reader = csv.reader(FILE)
                next(reader, None)
                for row in reader:
                    CitiesData.objects.create(name=row[1],
                                              region=row[0],
                                              data=row[2])
