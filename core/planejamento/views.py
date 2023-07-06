import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from core.perfil.views import Categoria


def definir_planejamento(request):
    categorias = Categoria.objects.all()
    return render(
        request,
        'definir_planejamento.html',
        {
            'categorias': categorias,
        },
    )


# não vai receber o csrf_token
@csrf_exempt
def update_valor_categoria(request, id):
    novo_valor = json.load(request)['novo_valor']
    categoria = Categoria.objects.get(id=id)
    categoria.valor_planejamento = novo_valor
    categoria.save()

    return JsonResponse({'status': 'Sucesso'})


def ver_planejamento(request):
    categorias = Categoria.objects.all()
    return render(request, 'ver_planejamento.html', {'categorias': categorias})
