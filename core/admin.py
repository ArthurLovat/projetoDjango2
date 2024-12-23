from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProudtoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'slug', 'criado', 'modificado', 'ativo')
