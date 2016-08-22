from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the Sploodl index.")

def listView(request, uuid):
    return HttpResponse("There are %d transactions recorded in %s" % (1, uuid))

