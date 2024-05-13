from django.shortcuts import render, redirect, get_object_or_404
from app.forms import ClienteForm, ServicoForm
from .models import Cliente, Servico





def home(request):
    return render(request, 'home.html')

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'app/cliente_list.html', {'clientes': clientes})

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'app/cliente_form.html', {'form': form})

def cliente_edit(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'app/cliente_form.html', {'form': form})

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'app/cliente_confirm_delete.html', {'cliente': cliente })


#def cliente_delete(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    cliente.delete()
    return redirect('cliente_list')

def servico_list(request):
    servicos = Servico.objects.all()
    return render(request, 'app/servico_list.html', {'servicos': servicos})

def servico_create(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('servico_list')
    else:
        form = ServicoForm()
    return render(request, 'app/servico_form.html', {'form': form})

def servico_edit(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        form = ServicoForm(request.POST, request.FILES, instance=servico)
        if form.is_valid():
            form.save()
            return redirect('servico_list')
    else:
        form = ServicoForm(instance=servico)
    return render(request, 'app/servico_form.html', {'form': form})

def servico_delete(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        servico.delete()
        return redirect('servico_list')
    return render(request, 'app/servico_confirm_delete.html', {'servico': servico})