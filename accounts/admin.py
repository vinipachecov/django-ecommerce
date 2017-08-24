


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

# importar o modelo do nosso usuário criado
from .models import User

# Importando o tipo de formulario que criamos em accounts.forms.py
from .forms import UserAdminCreationForm, UserAdminForm



#  configurações do admin para o usuárioem nossa nova app accounts -> USER
class UserAdmin(BaseUserAdmin):

    add_form = UserAdminCreationForm
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password1', 'password2')
        }),
    )
    form = UserAdminForm
    fieldsets = (
        (None, {
            'fields': ('username', 'email')
        }),
        ('Informações Básicas', {
            'fields': ('name', 'last_login')
        }),
        (
            'Permissões', {
                'fields': (
                    'is_active', 'is_staff', 'is_superuser', 'groups',
                    'user_permissions'
                )
            }
        ),
    )
    list_display = ['username', 'name', 'email', 'is_active', 'is_staff', 'date_joined']



admin.site.register(User, UserAdmin)
