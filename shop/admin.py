from django.contrib import admin
from .models import Brand, Type, Cream

class Brand_admin (admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class Type_admin (admin.ModelAdmin):
    readonly_fields = ('created', 'updated')   

class Cream_admin (admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Brand, Brand_admin)
admin.site.register(Type, Type_admin)
admin.site.register(Cream, Cream_admin)

