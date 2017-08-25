
from django.conf.urls import url


from . import views


#  observe que views.OBJETOCHAMADO
# register é o nome da variável que instancia a view no
# arquivo views.py da aplicação accounts
# poderia ser substituido por views.RegisterView.as_view
urlpatterns = [
    url(r'^registro/$', views.register, name='register')
]
