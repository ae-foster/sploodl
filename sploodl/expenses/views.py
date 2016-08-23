from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import *

def index(request):
    return HttpResponse("Hello, world. You're at the Sploodl index.")

def listView(request, uuid):
    sploodl = get_object_or_404(Sploodl, id=uuid)
    latest_transaction_list = sploodl.transaction_set.order_by('-dateCreated')[:20]
    print(latest_transaction_list[0])
    return render(request, 'expenses/list.html', {'sploodl': sploodl,
                                                  'latest_transaction_list': latest_transaction_list})

def balanceView(request, uuid):
    sploodl = get_object_or_404(Sploodl, id=uuid)
    return render(request, 'expenses/balances.html', {'sploodl': sploodl})


