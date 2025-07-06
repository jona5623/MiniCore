from django.shortcuts import render, redirect, get_object_or_404
from ventas.forms import ReglasForms
from ventas.models import Reglas


def reglas_list(request):
    reglas = Reglas.objects.all()
    return render(request, 'reglas/reglas_list.html', {'reglas': reglas})

def reglas_create(request):
    if request.method == 'POST':
        form = ReglasForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reglas_list')
    else:
        form = ReglasForms()
    return render(request, 'reglas/reglas_form.html', {'form': form})

def reglas_update(request, pk):
    regla = get_object_or_404(Reglas, pk=pk)
    if request.method == 'POST':
        form = ReglasForms(request.POST, instance=regla)
        if form.is_valid():
            form.save()
            return redirect('reglas_list')
    else:
        form = ReglasForms(instance=regla)
    return render(request, 'reglas/reglas_form.html', {'form': form})

def reglas_delete(request, pk):
    regla = get_object_or_404(Reglas, pk=pk)
    if request.method == 'POST':
        regla.delete()
        return redirect('reglas_list')
    return render(request, 'reglas/reglas_confirm_delete.html', {'object': regla})