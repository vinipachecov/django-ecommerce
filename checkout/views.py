# coding=utf-8

from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView, TemplateView
from django.forms import modelformset_factory
from django.contrib import messages
from django.core.urlresolvers import reverse
from catalog.models import Product
from .models import CartItem

# need a redirect url
class CreateCartItemView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        # get the product
        product = get_object_or_404(Product, slug=self.kwargs['slug'])
        if self.request.session.session_key is None:
            self.request.session.save()
        cart_item, created = CartItem.objects.add_item(
            self.request.session.session_key, product
        )
        if created:
            messages.success(self.request, 'Produto adicionado com suesso')
        else:
            messages.success(self.request, 'Produto atualizado com suesso')
        return reverse('checkout:cart_item')

        # django does not have redirect for formset


class CartItemView(TemplateView):

    template_name = 'checkout/cart.html'

    def get_formset(self, clear=False):
        CartItemFormSet = modelformset_factory(
            CartItem, fields=('quantity',), can_delete=True, extra=0
        )
        session_key = self.request.session.session_key
        if session_key:
            if clear:
                # doesn't have a post because we want to clear
                formset = CartItemFormSet(
                queryset=CartItem.objects.filter(cart_key=session_key))
            else:
                formset = CartItemFormSet(
                queryset=CartItem.objects.filter(cart_key=session_key),
                    data=self.request.POST or None
                )
        else:
            formset = CartItemFormSet(queryset=CartItem.objects.none())
        return formset

    def get_context_data(self, **kwargs):
        context = super(CartItemView, self).get_context_data(**kwargs)
        context['formset'] = self.get_formset()
        return context

    # submission of my formset
    def post(self,request, *args, **kwargs):
        formset = self.get_formset()
        context = self.get_context_data(**kwargs)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Carrinho atualizado com sucesso')
            # update the cart items in case the user deletes withouth a redirect
            context['formset'] = self.get_formset(clear=True)

        return self.render_to_response(context)


create_cartitem = CreateCartItemView.as_view()
cart_item = CartItemView.as_view()