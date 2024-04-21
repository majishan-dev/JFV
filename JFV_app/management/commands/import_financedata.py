import csv
from django.core.management.base import BaseCommand
from ...models import FinanceData

class Command(BaseCommand):
    help = 'Loads data from a specific CSV file into the FinanceData model'

    def handle(self, *args, **options):
        # プロジェクトのルートからの相対パス
        file_path = 'JFV_app/management/data/finance_data.csv'

        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                _, created = FinanceData.objects.update_or_create(
                    year=int(row[0]),
                    defaults={'revenue': float(row[1]), 'expenditure': float(row[2])}
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully added finance data for year {row[0]}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Updated finance data for year {row[0]}'))
