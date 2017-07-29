from django.contrib import admin

# Register your models here.

from .models import Product, Category

# forma de lista
# admin.site.register([Product,Category])
# individual


class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name','slug','created' ,'modified']
    search_fields = ['name' , 'slug']
    list_filter = ['created', 'modified']

class ProductAdmin(admin.ModelAdmin):

    list_display = ['name','slug','category','created' ,'modified']
    search_fields = ['name' , 'slug', 'category__name']
    list_filter = ['created', 'modified']

    # funcoes das opcoes selecionadas
    # actions...

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
