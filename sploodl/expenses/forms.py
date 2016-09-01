from django import forms
from expenses.models import *
from .currency.converter import CURRENCIES


class SploodlForm(forms.Form):
    name = forms.CharField(label='Title', max_length=140)
    homeCurrency = forms.ChoiceField(choices = CURRENCIES, label="Home currency")
    participants = forms.CharField(label = 'Participants names (comma separated)')


class TransactionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        sploodl = kwargs.pop('sploodl')
        super(TransactionForm, self).__init__(*args, **kwargs)
        # snip the other fields for the sake of brevity
        # Adding content to the form
        self.fields['people_by'].queryset = sploodl.participant_set.all()
        self.fields['people_for'].queryset = sploodl.participant_set.all()
        self.fields['people_for'].initial = sploodl.participant_set.all()

    class Meta:
        model = Transaction
        fields = ['description', 'currency', 'value', 'people_by', 'people_for']

