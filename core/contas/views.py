from datetime import datetime

from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import redirect, render

from core.perfil.models import Categoria

from .models import ContaPaga, ContaPagar


def definir_contas(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        return render(
            request,
            'definir_contas.html',
            {
                'categorias': categorias,
            },
        )
    else:
        titulo = request.POST.get('titulo')
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        valor = request.POST.get('valor')
        dia_pagamento = request.POST.get('dia_pagamento')

        def __str__(self):
            return self.titulo

        conta = ContaPagar(
            titulo=titulo,
            categoria_id=categoria,
            descricao=descricao,
            valor=valor,
            dia_pagamento=dia_pagamento,
        )

        conta.save()

        messages.add_message(
            request,
            constants.SUCCESS,
            'Conta cadastrada com sucesso',
        )
        return redirect('/contas/definir_contas')


def ver_contas(request):
    MES_ATUAL = datetime.now().month
    DIA_ATUAL = datetime.now().day

    # buscar todas as contas
    contas = ContaPagar.objects.all()

    # contas já pagas etraz a conta que foi paga
    contas_pagas = ContaPaga.objects.filter(
        data_pagamento__month=MES_ATUAL
    ).values('conta')

    # excluir as contas que ja foram pagas com data LessThen
    contas_vencidas = contas.filter(dia_pagamento__lt=DIA_ATUAL).exclude(
        id__in=contas_pagas
    )

    # as contas proximas do vencimento com cinco dias
    contas_proximas_vencimento = (
        contas.filter(dia_pagamento__lte=DIA_ATUAL + 5)
        .filter(dia_pagamento__gte=DIA_ATUAL)
        .exclude(id__in=contas_pagas)
    )

    # as contas restantes
    restantes = (
        contas.exclude(id__in=contas_vencidas)
        .exclude(id__in=contas_pagas)
        .exclude(id__in=contas_proximas_vencimento)
    )

    return render(
        request,
        'ver_contas.html',
        {
            'contas_vencidas': contas_vencidas,
            'contas_proximas_vencimento': contas_proximas_vencimento,
            'restantes': restantes,
        },
    )
