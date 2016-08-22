from __future__ import unicode_literals

from django.db import models

CURRENCIES = [('GBP', 'British Pound Sterling'),
                ('USD', 'United States Dollar'),
                ('EUR', 'Euro'),
                ('DKK', 'Danish Krone'),
                ('SEK', 'Swedish Krona')]


class Sploodl(models.Model):
    name = models.CharField(max_length=140)
    home_currency = models.CharField(max_length=3, choices = CURRENCIES)



class Participant(models.Model):
    sploodl = models.ForeignKey(Sploodl, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)

class Transaction(models.Model):
    sploodl = models.ForeignKey(Sploodl, on_delete=models.CASCADE)
    description = models.CharField(max_length=140)
    currency = models.CharField(max_length=3, choices = CURRENCIES)
    people_by = models.ManyToManyField(Participant, related_name='+')
    people_for = models.ManyToManyField(Participant, related_name='+')
    value = models.DecimalField(max_digits=12, decimal_places=2)
