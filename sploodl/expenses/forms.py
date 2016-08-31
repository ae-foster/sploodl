from django import forms
from expenses.models import Sploodl, Participant

CURRENCIES = [('GBP', 'British Pound Sterling'),
                ('USD', 'United States Dollar'),
                ('EUR', 'Euro'),
                ('DKK', 'Danish Krone'),
                ('SEK', 'Swedish Krona')]

class SploodlForm(forms.Form):
    name = forms.CharField(label='Title', max_length=140)
    homeCurrency = forms.ChoiceField(choices = CURRENCIES, label="Home currency")
    participants = forms.CharField(label="Participants (comma separated)", max_length=900)



