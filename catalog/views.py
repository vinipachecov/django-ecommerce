from django.shortcuts import render , get_object_or_404
from django.views import generic

# Create your views here.

from .models import Product, Category

class ProductListView(generic.ListView):
    #  generic.Listview serve para listar coisas

    queryset = Product.objects.all()
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'


# def product_list(request):
#     context = {
#         'product_list': Product.objects.all()
#     }
#     return render(request, 'catalog/product_list.html',context)


class CategoryListView(generic.ListView):

    template_name = 'catalog/category.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        # verifica se existe uma variavel chamada model
        #  se existe ela faz model.objet.all()
        # se existe a variavel query set
        # category = get_object_or_404(Category, slug=self.kwargs['slug'])
        # filtrando pela categoria
        # return Product.objects.filter(category=category)
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category,slug=self.kwargs['slug'])
        return context


def category(request, slug):
    category = Category.objects.get(slug=slug)
    context = {
        'current_category': category,
        'product_list': Product.objects.filter(category=category),
    }
    return render(request,'catalog/category.html',context)


def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request,'catalog/product.html', context)

# Instancias

product_list = ProductListView.as_view()
category = CategoryListView.as_view()
