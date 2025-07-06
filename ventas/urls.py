from django.urls import path
from ventas.views.VentasViews import (ventas_list, ventas_create, ventas_update, ventas_delete, reporte_comisiones)
from ventas.views.VendedorViews import (vendedor_list, vendedor_create, vendedor_update, vendedor_delete)
from ventas.views.ReglasViews import (reglas_list, reglas_create, reglas_update, reglas_delete)

urlpatterns = [

    path('reglas/', reglas_list, name='reglas_list'),
    path('reglas/crear/', reglas_create, name='reglas_create'),
    path('reglas/<int:pk>/editar/', reglas_update, name='reglas_update'),
    path('reglas/<int:pk>/eliminar/', reglas_delete, name='reglas_delete'),

    path('vendedores/', vendedor_list, name='vendedor_list'),
    path('vendedores/crear/', vendedor_create, name='vendedor_create'),
    path('vendedores/<int:pk>/editar/', vendedor_update, name='vendedor_update'),
    path('vendedores/<int:pk>/eliminar/', vendedor_delete, name='vendedor_delete'),

    path('ventas/', ventas_list, name='ventas_list'),
    path('ventas/crear/', ventas_create, name='ventas_create'),
    path('ventas/<int:pk>/editar/', ventas_update, name='ventas_update'),
    path('ventas/<int:pk>/eliminar/', ventas_delete, name='ventas_delete'),
    path('reporte-comisiones/', reporte_comisiones, name='reporte_comisiones'),
]