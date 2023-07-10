Em home busque os dados e envie no context:

```python
valores = Valores.objects.filter(data__month=datetime.now().month)
entradas = valores.filter(tipo='E')
saidas = valores.filter(tipo='S')

total_entradas = calcula_total(entradas, 'valor')
total_saidas = calcula_total(saidas, 'valor')
```

Altere em home.html os valores e os redirecionamentos.

Crie a função calcula_equilibrio_financeiro:

```python
def calcula_equilibrio_financeiro():
    gastos_essenciais = Valores.objects.filter(data__month=datetime.now().month).filter(tipo='S').filter(categoria__essencial=True)
    gastos_nao_essenciais = Valores.objects.filter(data__month=datetime.now().month).filter(tipo='S').filter(categoria__essencial=False)

    total_gastos_essenciais = calcula_total(gastos_essenciais, 'valor')
    total_gastos_nao_essenciais = calcula_total(gastos_nao_essenciais, 'valor')

    total = total_gastos_essenciais + total_gastos_nao_essenciais
    try:
        percentual_gastos_essenciais = total_gastos_essenciais * 100 / total
        percentual_gastos_nao_essenciais = total_gastos_nao_essenciais * 100 / total

        return percentual_gastos_essenciais, percentual_gastos_nao_essenciais
    except:
        return 0, 0
```

Chame a função na view e envie para o context:

```python
percentual_gastos_essenciais, percentual_gastos_nao_essenciais = calcula_equilibrio_financeiro()
```