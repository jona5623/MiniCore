from django.shortcuts import render, redirect, get_object_or_404
from ventas.forms import VentasForms, ReporteForms
from ventas.models import Ventas



# CRUD para Ventas
def ventas_list(request):
    ventas = Ventas.objects.select_related('vendedor', 'regla').all()
    return render(request, 'ventas/ventas_list.html', {'ventas': ventas})

def ventas_create(request):
    if request.method == 'POST':
        form = VentasForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ventas_list')
    else:
        form = VentasForms()
    return render(request, 'ventas/ventas_form.html', {'form': form})

def ventas_update(request, pk):
    venta = get_object_or_404(Ventas, pk=pk)
    if request.method == 'POST':
        form = VentasForms(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('ventas_list')
    else:
        form = VentasForms(instance=venta)
    return render(request, 'ventas/ventas_form.html', {'form': form})

def ventas_delete(request, pk):
    venta = get_object_or_404(Ventas, pk=pk)
    if request.method == 'POST':
        venta.delete()
        return redirect('ventas_list')
    return render(request, 'ventas/ventas_confirm_delete.html', {'object': venta})


def reporte_comisiones(request):
    ventas_filtradas = []
    total_comision = 0
    form = ReporteForms(request.GET or None)

    if form.is_valid():
        fecha_inicio = form.cleaned_data['fecha_inicio']
        fecha_fin = form.cleaned_data['fecha_fin']
        ventas_filtradas = Ventas.objects.filter(fecha__gte=fecha_inicio, fecha__lte=fecha_fin)

        for venta in ventas_filtradas:
            if venta.regla:
                comision = venta.monto * (venta.regla.comision / 100)
                total_comision += comision
    else:
        ventas_filtradas = None

    return render(request, 'ventas/reporte_comisiones.html', {
        'form': form,
        'ventas': ventas_filtradas,
        'total_comision': total_comision
    })