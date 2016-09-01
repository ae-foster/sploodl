from __future__ import unicode_literals
import uuid
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save, pre_delete

from .currency.converter import convertValue, CURRENCIES

#CURRENCIES = [('GBP', 'British Pound Sterling'),
#                ('USD', 'United States Dollar'),
#                ('EUR', 'Euro'),
#                ('DKK', 'Danish Krone'),
#                ('SEK', 'Swedish Krona')]


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

    def balance(self):
        return sum([iou.value for iou in self.iou_set.all()])


class Transaction(models.Model):
    sploodl = models.ForeignKey(Sploodl, on_delete=models.CASCADE)
    dateCreated = models.DateTimeField(default = timezone.now)
    dateModified = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=140)
    currency = models.CharField(max_length=3, choices = CURRENCIES)
    people_by = models.ManyToManyField(Participant,related_name='+')
    people_for = models.ManyToManyField(Participant,related_name='+')
    value = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.description

    def refreshIOUs(self):
        #Delete IOUs
        self.deleteIOUs()

        # Create IOUs
        self.createIOUs()

        #Update date modified
        self.dateModified = timezone.now()


    def deleteIOUs(self):
        #Delete IOUs
        for iou in self.iou_set.all():
            iou.delete()


    def createIOUs(self):
        #Currency conversion
        self.valueInHomeCurrency = convertValue(float(self.value),
                                            self.currency, self.sploodl.home_currency)

        # Credit
        by_query_set = self.people_by.get_queryset()
        divisor = len(by_query_set)
        for participant in by_query_set:
            i=IOU(sploodl = self.sploodl, participant = participant, transaction = self,
                value = self.valueInHomeCurrency/divisor)
            i.save()

        # Debit
        for_query_set = self.people_for.get_queryset()
        divisor = len(for_query_set)
        for participant in for_query_set:
            i= IOU(sploodl = self.sploodl, participant = participant, transaction = self,
                value = -1*self.valueInHomeCurrency/divisor)
            i.save()


def model_created_or_updated(sender, **kwargs):
    the_instance = kwargs['instance']
    the_instance.refreshIOUs()

post_save.connect(model_created_or_updated, sender=Transaction)

def model_deleted(sender, **kwargs):
    the_instance = kwargs['instance']
    the_instance.deleteIOUs()

pre_delete.connect(model_deleted, sender=Transaction)


class IOU(models.Model):
    sploodl = models.ForeignKey(Sploodl, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.participant.name + " " + str(self.value)

