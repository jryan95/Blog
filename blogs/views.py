from django.shortcuts import render

def index(request):
    """ Blog homepage. """
    return render(request, 'templates/index.html')

