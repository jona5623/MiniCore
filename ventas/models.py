# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Reglas(models.Model):
    id = models.BigAutoField(primary_key=True)
    monto_minimo = models.DecimalField(max_digits=10, decimal_places=2)
    monto_maximo = models.DecimalField(max_digits=10, decimal_places=2)
    comision = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'reglas'


class Vendedor(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.TextField()
    email = models.TextField()
    telefono = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendedor'


class Ventas(models.Model):
    id = models.BigAutoField(primary_key=True)
    vendedor = models.ForeignKey(Vendedor, models.DO_NOTHING)
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    regla = models.ForeignKey(Reglas, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ventas'
