# MiniCore

MiniCore es una aplicación web desarrollada en Django que permite gestionar vendedores, ventas y reglas de comisión.
Permite realizar operaciones CRUD sobre cada entidad y ofrece un reporte de comisiones generadas por ventas en un rango de fechas.

## Características principales

- Gestión de **vendedores** (alta, baja, modificación, listado)
- Gestión de **ventas**, vinculadas a un vendedor y una regla de comisión
- Gestión de **reglas de comisión** (por rango de montos)
- **Reporte de comisiones**: Filtra ventas por rango de fechas y calcula la comisión total correspondiente

## Estructura del proyecto

- **Vendedor**: Nombre, email, teléfono.
- **Reglas**: Monto mínimo, máximo y porcentaje de comisión.
- **Ventas**: Vendedor, fecha, monto y regla aplicada.
