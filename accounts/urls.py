
from django.conf.urls import url


from . import views


#  observe que views.OBJETOCHAMADO
# register é o nome da variável que instancia a view no
# arquivo views.py da aplicação accounts
# poderia ser substituido por views.RegisterView.as_view
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^alterar_dados/$', views.update_user, name='update_user'),
    url(r'^alterar_senha/$', views.update_password, name='update_password'),
    url(r'^registro/$', views.register, name='register')
]
