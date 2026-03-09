
from django.contrib import admin
from . models import Usuario
from django.contrib.auth.admin import UserAdmin

campos = list(UserAdmin.fieldsets)
campos.append(
    ("Historico", {'fields':('filme_vistos',)})
)

UserAdmin.fieldsets = tuple(campos)

admin.site.register(Usuario, UserAdmin)
