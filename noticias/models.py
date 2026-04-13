from django.db import models

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    corpo = models.TextField()

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    # O ForeignKey liga o comentário a um artigo específico
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário em {self.artigo.titulo}"