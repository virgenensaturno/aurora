from django.db import models
class Brand (models.Model):
    title = models.CharField(max_length=50)
    RAITING = [
        (1, "Muy mala"),
        (2, "Mala"),
        (3, "Buena"),
        (4, "Muy Buena"),
        (5, "Exelente"),
    ]
    raiting = models.PositiveBigIntegerField(choices= RAITING, default= 1, max_length=5)
    # Quisiera que raiting me de solo 5 posibilidades ¿cómo hago? 1:07
    created = models.DateField(auto_now_add = True)
    updated = models.DateField(auto_now=True)

class Type (models.Model):
    title = models.CharField(max_length=50, default= "")
    description = models.TextField(max_length=150, default="")
    created = models.DateField(auto_now_add =True)
    updated = models.DateField(auto_now=True)

class Cream (models.Model):
    title = models.CharField(max_length=50, default="")
    RAITING = [
        (1, "Muy mala"),
        (2, "Mala"),
        (3, "Buena"),
        (4, "Muy Buena"),
        (5, "Exelente"),
    ]
    raiting = models.PositiveBigIntegerField(RAITING, default= 1, max_length=5)
    description = models.TextField(max_length=150)
    created = models.DateField(auto_now_add =True)
    updated = models.DateField(auto_now=True)
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE,default="")
    type = models.ForeignKey(Type, on_delete = models.CASCADE, default="")
    image = models.ImageField(upload_to= "cover", null = True, blank= True)