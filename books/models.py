from datetime import date

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    isbn = models.CharField('ISBN', max_length=13)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    publish_date = models.DateField(default=date.today)

    def __str__(self):
        return self.title


