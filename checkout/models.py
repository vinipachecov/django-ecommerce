# coding=utf-8

from pagseguro import PagSeguro

from django.db import models
from django.conf import settings

from catalog.models import Product


class CartItemManager(models.Manager):

    def add_item(self, cart_key, product):
        if self.filter(cart_key=cart_key, product=product).exists():
            created = False
            cart_item = self.get(cart_key=cart_key, product=product)
            cart_item.quantity = cart_item.quantity + 1
            cart_item.save()
        else:
            created = True
            cart_item = CartItem.objects.create(
            cart_key=cart_key, product=product, price=product.price
            )

        # cart_item, created = self.get_or_create(cart_key=cart_key, product= product)
        return cart_item, created



class CartItem(models.Model):

    cart_key = models.CharField(
                'Chave do Carrinho', max_length=40, db_index=True
                )
    product = models.ForeignKey('catalog.Product', verbose_name='Produto')
    quantity = models.PositiveIntegerField('Quantidade', default=1)
    price = models.DecimalField('Preço',max_digits=8, decimal_places=2)

    objects = CartItemManager()

    class Meta:
        verbose_name = 'Item do Carrinho'
        verbose_name_plural = 'Itens dos Carrinhos'
        unique_together = (('cart_key', 'product'), )

    def __str__(self):
        return '{} [{}]'.format(self.product, self.quantity)


class OrderManager(models.Manager):

    def create_order(self, user, cart_items):
        order = self.create(user=user)
        for cart_item in cart_items:
            order_item = OrderItem.objects.create(
                order=order, quantity=cart_item.quantity,
                product=cart_item.product,
                price= cart_item.price
            )
        return order


class Order(models.Model):

    STATUS_CHOICES = (
        (0, 'Aguardando Pagamento'),
        (1, 'Concluída'),
        (2, 'Cancelada'),
    )

    PAYMENT_OPTION_CHOICES = (
        ('deposit', 'Depósito'),
        ('pagseguro', 'Pagseguro'),
        ('paypal', 'Paypal'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário')
    status = models.IntegerField(
        'Situação', choices=STATUS_CHOICES, default=0, blank=True
    )
    payment_option = models.CharField(
        'Opção de pagamento', choices=PAYMENT_OPTION_CHOICES, max_length=20,
        default='deposit'
    )
    created = models.DateTimeField('Criado em ', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now_add=True)

    objects = OrderManager()

    class Meta:
        verbose_name ='Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return 'Pedido #{}'.format(self.pk)

    def products(self):
        products_ids = self.items.values_list('product')
        return Product.objects.filter(pk__in=products_ids)

    def total(self):
        aggregate_queryset = self.items.aggregate(
            total=models.Sum(
                models.F('price') * models.F('quantity'),
                output_field=models.DecimalField()
            )
        )
        return aggregate_queryset['total']

    def pagseguro(self):
        self.payment_option = 'pagseguro'
        self.save()
        pg = PagSeguro(
            email=settings.PAGSEGURO_EMAIL, token=settings.PAGSEGURO_TOKEN,
            config={'sandbox': settings.PAGSEGURO_SANDBOX}
        )
        # print('useremail = {} PAGSEGURO_TOKEN = {}, PAGSEGURO_EMAIL = {}'.format(self.user.email,
        #     settings.PAGSEGURO_TOKEN, settings.PAGSEGURO_EMAIL))
        pg.sender = {
            'email' : self.user.email
        }
        pg.reference_prefix = None
        pg.shipping = None
        pg.reference = self.pk
        print('self.pk = {}'.format(self.pk))
        for item in self.items.all():
            print(item.product.name)
            pg.items.append(
                {
                    'id': item.product.pk,
                    'description': item.product.name,
                    'quantity': item.quantity,
                    'amount': '%.2f' % item.price
                }
            )
        return pg

    def paypal(self):
        paypal_dict = {
            'upload': '1',
            'business': settings.PAYPAL_EMAIL,
            'invoice': self.pk,
            'cmd': '_cart',
            'currency_code': 'BRL',
            'charset': 'utf-8',
        }
        index = 1
        for item in self.items.all():
            paypal_dict['amount_{}'.format(index)] = '%.2f' % item.price
            paypal_dict['item_name_{}'.format(index)] = item.product.name
            paypal_dict['quantity_{}'.format(index)] = item.quantity
            index = index + 1
        return paypal_dict




class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name='Pedido', related_name='items')
    product = models.ForeignKey('catalog.Product', verbose_name='Produto')
    quantity = models.PositiveIntegerField('Quantidade', default=1)
    price = models.DecimalField('Preço',max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens dos Pedidos'

    def __str__(self):
        return '[{}] Produto'.format(self.order.pk, self.product)



        # products = []
        # for item in self.items.all():
        #     # get all products from orderitem
        #     products.append(item.product)
        # return products

# delete the item in the cart if the user lower the value below 1
def post_save_cart_item(instance, **kwargs):
    if instance.quantity < 1:
        instance.delete()

models.signals.post_save.connect(
    post_save_cart_item, sender=CartItem, dispatch_uid='post_save_cart_item'
)
