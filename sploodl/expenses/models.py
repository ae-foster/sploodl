from __future__ import unicode_literals

from django.db import models

CURRENCIES = {'GBP': 'British Pound Sterling',
              'USD': 'United States Dollar',
              'EUR': 'Euro',
              'DKK': 'Danish Krone',
              'SEK': 'Swedish Krona'}


class Sploodl(models.Model):
    home_currency = models.CharField(max_length=3, choices = CURRENCIES.keys())


class Participant(models.Model):
    sploodl = models.ForeignKey(Sploodl, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)

class Transaction(models.Model):
    sploodl = models.ForeignKey(Sploodl, on_delete=models.CASCADE)
    description = models.CharField(max_length=140)
    currency = models.CharField(max_length=3, choices = CURRENCIES.keys())
    people_by = models.ManyToManyField(Participant)
    people_for = models.ManyToManyField(Participant)
    value = models.DecimalField(max_digits=12, decimal_places=2)
