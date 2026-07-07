from django.contrib import admin
from blog.models import Categoria, Post

class CategoriaAdmin(admin.ModelAdmin):
    list_display  = ('nome_categoria',)
    search_fields = ('nome_categoria',)

class PostAdmin(admin.ModelAdmin):
    list_display  = ('titulo', 'autor', 'categoria', 'data_publicacao')
    search_fields = ('titulo', 'autor')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post,      PostAdmin)