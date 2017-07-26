from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Em um metodo function based view
#  cada view (pagina) tem como referencia uma funcao
# em uma determinada aplicacao
def index(request):

    # Variaveis e seus valore estaticos para
    #  o template dessa view especifica
    return render(request, 'index.html')


def contact(request):

    # Variaveis e seus valore estaticos para
    #  o template dessa view especifica
    return render(request, 'contact.html')


def product_list(request):

    # Variaveis e seus valore estaticos para
    #  o template dessa view especifica
    return render(request, 'product_list.html')


def product(request):

    # Variaveis e seus valore estaticos para
    #  o template dessa view especifica
    return render(request, 'product.html')
