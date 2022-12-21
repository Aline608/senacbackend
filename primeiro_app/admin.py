from django.contrib import admin
from primeiro_app.models import Autor, Categoria, Livro


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    ...


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    ...


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    ...

# Register your models here.
