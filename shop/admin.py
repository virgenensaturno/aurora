from django.contrib import admin
from.models import Type, Brand, Cream

class Type_admin(admin.ModelAdmin):
    list_filter =('name',)

class Brand_admin(admin.ModelAdmin):
    list_filter =('name',)

class Cream_admin(admin.ModelAdmin):
    list_filter =('name',)

admin.site.register(Type, Type_admin)
admin.site.register(Brand, Brand_admin)
admin.site.register(Cream, Cream_admin)
