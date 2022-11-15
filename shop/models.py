from django.db import models

class Brand (models.Model):
    name = models.CharField(max_length=100)
    
class Cream(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    RAITING = [
        (1, 'Muy mala'),
        (2, 'Mala'),
        (3, 'Buena'),
        (4, 'Muy buena'),
        (5, 'Excelente'),
    ]
    raiting = models.PositiveBigIntegerField(choices = RAITING,default=1)
    image = models.ImageField(upload_to="shop", null=True, blank=True)

class Type (models.Model):
    name = models.CharField(max_length=100)
    cream = models.ForeignKey(Cream, verbose_name=("Crema"), on_delete=models.CASCADE, default='')