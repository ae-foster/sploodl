from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


from .models import *
from .forms import *


def index(request):
    return HttpResponse("Hello, world. You're at the Sploodl index.")

def listView(request, uuid):
    sploodl = get_object_or_404(Sploodl, id=uuid)
    latest_transaction_list = sploodl.transaction_set.order_by('-dateCreated')[:20]
    if request.method == 'POST':
        form = TransactionForm(request.POST, sploodl=sploodl, auto_id=False)
        if form.is_valid():
            new_transaction = form.save(commit=False)
            new_transaction.sploodl = sploodl
            new_transaction.dateCreated = timezone.now()
            new_transaction.dateModified = timezone.now()
            new_transaction.save()
            form.save_m2m()
            new_transaction.createIOUs()

        return HttpResponseRedirect(reverse('expenses:list', args = (sploodl.id,)))
    else:
        add_another = TransactionForm(sploodl=sploodl, auto_id=False)
        return render(request, 'expenses/list.html', {'sploodl': sploodl,
                                                      'add_form': add_another,
                                                      'latest_transaction_list': latest_transaction_list})


def balanceView(request, uuid):
    sploodl = get_object_or_404(Sploodl, id=uuid)
    return render(request, 'expenses/balances.html', {'sploodl': sploodl})


def delete(request, uuid, id):
    sploodl = get_object_or_404(Sploodl, id=uuid)
    get_object_or_404(Transaction, id = id).delete()
    return HttpResponseRedirect(reverse('expenses:list', args = (sploodl.id,)))


def createView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SploodlForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # Create the Sploodl instance
            name = form.cleaned_data['name']
            homeCurrency = form.cleaned_data['homeCurrency']
            participants = form.cleaned_data['participants']
            parti_list = [parti.strip() for parti in participants.split(",")]

            newSploodl = Sploodl(name=name, home_currency = homeCurrency)
            newSploodl.save()

            for parti in parti_list:
                new_participant = Participant(name = parti, sploodl = newSploodl)
                new_participant.save()


            return HttpResponseRedirect(reverse('expenses:list', args = (newSploodl.id,)))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SploodlForm()

    return render(request, 'expenses/create.html', {'spl_form': form})