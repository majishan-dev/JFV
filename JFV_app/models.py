from django.db import models

# Create your models here.
class FinanceData(models.Model):
    year = models.IntegerField(verbose_name="年度")
    revenue = models.FloatField(verbose_name="歳入額")
    expenditure = models.FloatField(verbose_name="歳出額")

    def __str__(self):
        return f"{self.year}年"