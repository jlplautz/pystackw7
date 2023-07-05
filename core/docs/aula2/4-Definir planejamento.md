Crie o app planejamento:

```python
python3 manage.py startapp planejamento
```

Crie a URL para definir_planejamento:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('definir_planejamento/', views.definir_planejamento, name="definir_planejamento"),
]
```

Crie a view definir_planejamento:

```python
def definir_planejamento(request):
    categorias = Categoria.objects.all()
    return render(request, 'definir_planejamento.html', {'categorias': categorias})
```

Crie o HTML definir_planejamento:

```python
{% extends 'bases/base.html' %}
{% load static %}
{% block 'head' %}

    <link href="{% static 'perfil/css/home.css' %}" rel="stylesheet">
    <link href="{% static 'perfil/css/gerenciar.css' %}" rel="stylesheet">
    <link href="{% static 'extrato/css/view_extrato.css' %}" rel="stylesheet">

{% endblock %}

{% block 'body' %}

    <div class="container">
        <br>
        <br>
        <p class="fonte-destaque">Definir planejamento</p>
        <div class="card">
        
            <table>
                <tr>
                    <th>Categoria</th>
                    <th>Valor</th>
                    <th>Ação</th>
                </tr>

                {% for categoria in categorias %}
                    <tr class="linha">
                        <td>{{categoria}}</td>
                        <td><input type="number" class="form-control" value="{{categoria.valor_planejamento}}"></td>
                        <td><button style="width: 100%;" class="botao-secundario">Salvar</button></td>         
                    </tr>
                {% endfor %}
                

            </table>
        

        </div>
    </div>

{% endblock %}
```

Crie a função JavaScript para enviar os dados:

```python
<script>

        function update_valor_planejamento_categoria(id){
            valor = document.getElementById('valor-categoria-'+id).value
            console.log(valor)

             fetch("/planejamento/update_valor_categoria/"+id, {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                    
                },
                body: JSON.stringify({novo_valor: valor})
                
            }).then(function(result){
                return result.json()

            }).then(function(data){
                console.log(data)

            })

        }

</script>
```

Chame a função no click do botão:

```python
onclick="update_valor_planejamento_categoria({{categoria.id}})"
```

Adicione o id no input:

```python
id="valor-categoria-{{categoria.id}}"
```

Crie a URL update_categoria:

```python
path('update_valor_categoria/<int:id>', views.update_valor_categoria, name="update_valor_categoria"),
```

Crie a VIEW:

```python
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def update_valor_categoria(request, id):
    novo_valor = json.load(request)['novo_valor']
    categoria = Categoria.objects.get(id=id)
    categoria.valor_planejamento = novo_valor
    categoria.save()

    return JsonResponse({'status': 'Sucesso'})
```