from __future__ import unicode_literals
import uuid

from django.db import models
from django.utils import timezone

CURRENCIES = [('GBP', 'British Pound Sterling'),
                ('USD', 'United States Dollar'),
                ('EUR', 'Euro'),
                ('DKK', 'Danish Krone'),
                ('SEK', 'Swedish Krona')]


class Sploodl(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=140)
    home_currency = models.CharField(max_length=3, choices = CURRENCIES)

    def __str__(self):
        return self.name


class Participant(models.Model):
    sploodl = models.ForeignKey(Sploodl, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    sploodl = models.ForeignKey(Sploodl, on_delete=models.CASCADE)
    date = models.DateTimeField(default = timezone.now)
    description = models.CharField(max_length=140)
    currency = models.CharField(max_length=3, choices = CURRENCIES)
    people_by = models.ManyToManyField(Participant, related_name='+')
    people_for = models.ManyToManyField(Participant, related_name='+')
    value = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.description

