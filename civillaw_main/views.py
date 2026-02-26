from django.shortcuts import render
from .models import Cliente

# Create your views here.

def index(request):
    """ pagina principal"""
    return render(request, 'civillaw_main/index.html')

def clientes(request):
    """ lista dos clientes cadastrados """
    clientes = Cliente.objects.order_by('clie_nome')
    context = {'clientes': clientes}
    return render(request, 'civillaw_main/clientes.html',context)
