Em perfil/urls.py crie uma URL para dashboard:

```python
path('dashboard/', views.dashboard, name="dashboard"),
```

Crie a view dashboard:

```python
def dashboard(request):
    dados = {}
    categorias = Categoria.objects.all()

    for categoria in categorias:
        dados[categoria.categoria] = Valores.objects.filter(categoria=categoria).aggregate(Sum('valor'))['valor__sum']

    return render(request, 'dashboard.html', {'labels': list(dados.keys()), 'values': list(dados.values())})
```

Crie a dashboard.html

```python
{% extends 'bases/base.html' %}
{% load static %}
{% block 'head' %}

    <link href="{% static 'perfil/css/home.css' %}" rel="stylesheet">
    <link href="{% static 'perfil/css/gerenciar.css' %}" rel="stylesheet">
    <link href="{% static 'contas/css/contas.css' %}" rel="stylesheet">

{% endblock %}

{% block 'body' %}

    <div class="container">
        <br>
        {% if messages %}
            {% for message in messages %}
                <div class="alert {{ message.tags }}">{{ message }}</div>
            {% endfor %}
        {% endif %}
        <br>
        <div class="row">

            <div class="col-md">
                <span class="fonte-destaque">Gastos por categoria</span>
                <div>
                    <canvas id="myChart"></canvas>
                </div>

            </div>

        </div>

    </div>

{% endblock %}
```

importe o chart.js

```python
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
```

Crie o JavaScript

```python
<script>
    const ctx = document.getElementById('myChart');

    new Chart(ctx, {
        type: 'bar',
        data: {
        labels: {{labels|safe}},
        datasets: [{
            label: 'Gastos por categoria',
            data: {{values}},
        }]
        },    
    });
</script>
```