from django.shortcuts import render, get_object_or_404, redirect
from .models import Artigo, Comentario

def lista_artigos(request):
    artigos = Artigo.objects.all()
    return render(request, 'noticias/lista.html', {'artigos': artigos})

def detalhe_artigo(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    return render(request, 'noticias/detalhe.html', {'artigo': artigo})

def comentarios_artigo(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    if request.method == "POST":
        texto = request.POST.get('texto')
        if texto:
            Comentario.objects.create(artigo=artigo, texto=texto)
        return redirect('comentarios_artigo', pk=pk)
    return render(request, 'noticias/comentarios.html', {'artigo': artigo})