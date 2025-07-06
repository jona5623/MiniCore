from django.shortcuts import render, redirect, get_object_or_404
from ventas.forms import VendedorForms
from ventas.models import Vendedor

# CRUD para Vendedor
def vendedor_list(request):
    vendedores = Vendedor.objects.all()
    return render(request, 'vendedor/vendedor_list.html', {'vendedores': vendedores})

def vendedor_create(request):
    if request.method == 'POST':
        form = VendedorForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendedor_list')
    else:
        form = VendedorForms()
    return render(request, 'vendedor/vendedor_form.html', {'form': form})

def vendedor_update(request, pk):
    vendedor = get_object_or_404(Vendedor, pk=pk)
    if request.method == 'POST':
        form = VendedorForms(request.POST, instance=vendedor)
        if form.is_valid():
            form.save()
            return redirect('vendedor_list')
    else:
        form = VendedorForms(instance=vendedor)
    return render(request, 'vendedor/vendedor_form.html', {'form': form})

def vendedor_delete(request, pk):
    vendedor = get_object_or_404(Vendedor, pk=pk)
    if request.method == 'POST':
        vendedor.delete()
        return redirect('vendedor_list')
    return render(request, 'vendedor/vendedor_confirm_delete.html', {'object': vendedor})