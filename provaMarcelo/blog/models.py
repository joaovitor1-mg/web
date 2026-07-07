from django.db import models

class Categoria(models.Model):
    id             = models.AutoField(primary_key=True)
    nome_categoria = models.CharField(max_length=200)

    def __str__(self):
        return self.nome_categoria

class Post(models.Model):
    id              = models.AutoField(primary_key=True)
    titulo          = models.CharField(max_length=200)
    conteudo        = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    autor           = models.CharField(max_length=200)
    imagem          = models.ImageField(upload_to='posts/', blank=True, null=True)
    categoria       = models.ForeignKey(Categoria,
                          on_delete=models.PROTECT,
                          related_name='posts_categoria')

    def __str__(self):
        return self.titulo
