from django.shortcuts import render

# Create your views here.

def index(request):
    """ pagina principal"""
    return render(request, 'civillaw_main/index.html')
