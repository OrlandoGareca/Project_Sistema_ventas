from django.db import models
from datetime import  datetime
# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=150,verbose_name='Nombre')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        db_table = 'tipo'
        ordering = ['id']

class Category(models.Model):
    name = models.CharField(max_length=150,verbose_name='Nombre')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categoria'
        ordering = ['id']

class Employee(models.Model):
    categ = models.ManyToManyField(Category)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    names = models.CharField(max_length=150,verbose_name="Nombre")
    dni = models.CharField(max_length=10,unique=True,verbose_name="Dni")
    date_joined  = models.DateField(default=datetime.now,verbose_name='Fecha de registro')
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(decimal_places=2, default=0.00, max_digits=9)
    state = models.BooleanField(default=True)
    gender = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatar/%d/%m/Y', null=True, blank=True)
    cvitae = models.FileField(upload_to='cvitae/%d/%m/Y', null=True, blank=True)

    def __str__(self):
        return self.names
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']