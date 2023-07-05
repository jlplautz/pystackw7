
Crie a URL para view_extrato:

```python
path('view_extrato/', views.view_extrato, name="view_extrato"),
```

Crie a view de view_extrato:

```python
def view_extrato(request):
    contas = Conta.objects.all()
    categorias = Categoria.objects.all()

        
    valores = Valores.objects.filter(data__month=datetime.now().month)
 

    return render(request, 'view_extrato.html', {'valores': valores, 'contas': contas, 'categorias': categorias})
```

Crie o HTML view_extrato:


```python
{% extends 'bases/base.html' %}
{% load static %}
{% block 'head' %}

    <link href="{% static 'perfil/css/home.css' %}" rel="stylesheet">
    <link href="{% static 'perfil/css/gerenciar.css' %}" rel="stylesheet">
    <link href="{% static 'extrato/css/view_extrato.css' %}" rel="stylesheet">

{% endblock %}

{% block 'body' %}
    <br>
    <br>
    <div class='container'>
        <form action="" method="GET">
        <div class="row">
            
            <div class="col-md">
                <label>Conta</label>
                <select name="conta" class="form-select">
                    {% for conta in contas %}
                        <option value="{{conta.id}}">{{conta}}</option>
                    {% endfor %}
                </select>
            </div>

            <div class="col-md">
                <label>Categoria</label>
                <select name="categoria" class="form-select">
                    {% for categoria in categorias %}
                        <option value="{{categoria.id}}">{{categoria}}</option>
                    {% endfor %}
                </select>
            </div>

            <div class="col-md">
                <label>Período</label>
                <select name="periodo" class="form-select">
                    <option>Últimos 7 dias</option>
                </select>
            </div>
        
            
        </div>
        <br>
        <div class="row">
            <div class="col-md-2">
                <input style="width: 100%" type="submit" class="botao-principal" value="Filtrar">
                
            </div>
            </form>
            <div class="col-md-2">
                <a href="" class="botao-secundario">Exportar extrato</a>
            </div>
        </div>
        <br>
        <br>

        <div class="card">
            
                <table>
                    <tr>
                        <th>Conta</th>
                        <th>Categoria</th>
                        <th>Data</th>
                        <th>Tipo</th>
                        <th>valor</th>
                        
                    </tr>
                    {% for valor in valores %}
                        <tr class="linha">
                            <td width="10%">{{valor.conta}}</td>
                            <td>{{valor.categoria}}</td>
                            <td>{{valor.data}}</td>
                            <td>
                            {% if valor.tipo == 'S'%}
                                <img src="{% static 'perfil/img/saidas.png' %}">
                            {% else %}
                                <img src="{% static 'perfil/img/entradas.png' %}">
                            {% endif %}
                            
                            </td>
                            <td>R$ {{valor.valor}}</td>
                            
                        </tr>
                    {% endfor %}

                </table>
            
        </div>
    </div>
{% endblock %}
```

Crie o css view_extrato.css:

```python
table{
    width: 100%;
    padding: 20px;
    text-align: center;

}

.linha{
    height: 40px;
    background-color: var(--dark-color);
    padding: 20px;
}

td, th{
    padding: 20px;
}

tr{
    background-color: var(--main-color);

}

.botao-secundario{

    background-color: transparent;
    color: white;
    text-decoration: none;
    border: 2px solid var(--contrast-color);
    padding: 10px;
    border-radius: 15px;
    width: 100%;
    display: block;
    text-align: center;

}
```

Atualize o formulário dos filtros:

```python
<form action="{% url 'view_extrato' %}" method="GET">
```

Realize os filtros nas views:

```python
conta_get = request.GET.get('conta')
categoria_get = request.GET.get('categoria')

if conta_get:
    valores = valores.filter(conta__id=conta_get)
if categoria_get:
    valores = valores.filter(categoria__id=categoria_get)
```