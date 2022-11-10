from django.db import models

# Create your models here.
#Tres tablas: Cremas-Corporales-Faciales-Manos. Relación many to man

class Type(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tipo")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha actualización")
    def __str__(self):
        return self.name

class Brand(models.Model):
    name= models.CharField(max_length=100, verbose_name="Marca")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha actualización")
    def __str__(self):
        return self.name

class Cream(models.Model):
    name= models.CharField(max_length=100, verbose_name="Crema")
    description = models.TextField(verbose_name="Descripción")
    RAITING = [
        (1,"Muy mala"),
        (2,"Mala"),
        (3,"Regular"),
        (4,"Buena"),
        (5,"Excelente"),
        
    ]
    rating = models.PositiveSmallIntegerField(choices= RAITING,verbose_name="Calificación")
    types = models.ManyToManyField(Type,verbose_name="Tipo")
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,verbose_name="Marca")
    image = models.ImageField(upload_to="products", null= True, blank= True,verbose_name="Caratula")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha actualización")
    def __str__(self):
        return self.name