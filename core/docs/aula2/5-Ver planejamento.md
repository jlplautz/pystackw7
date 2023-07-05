Crie a URL:

```python
path('ver_planejamento/', views.ver_planejamento, name="ver_planejamento")
```

Crie a view:

```python
def ver_planejamento(request):
    categorias = Categoria.objects.all()
    return render(request, 'ver_planejamento.html', {'categorias': categorias})
```

Crie o HTML ver_planejamento:

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
        <div class="row">
            <div class="col-md-2 text-center">
            </div>
            <div class="col-md">
               <div class="card">
                    {% for categoria in categorias %}
                        <p>{{categoria}}</p>
                        <div>
                        <span style="float: left !important;">R$ 10,00</span>
                        <span style="float: right !important;">R$ 25,00</span>
                        </div>
                        <div class="progress">
                            <div class="progress-bar progress-bar-striped bg-info" role="progressbar" style="width: 20%" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
                        </div>
                        <br>
                    {% endfor %}

                </div>
            </div>
            <div class="col-md-2 text-center">
            </div>
        </div>
    </div>

{% endblock %}
```

Adicione as funções na model Categoria:

```python
class Categoria(models.Model):
    categoria = models.CharField(max_length=50)
    essencial = models.BooleanField(default=False)
    valor_planejamento = models.FloatField(default=0)

    def __str__(self):
        return self.categoria
    
    def total_gasto(self):
        from extrato.models import Valores
        valores = Valores.objects.filter(categoria__id = self.id).filter(data__month=datetime.now().month).aggregate(Sum('valor'))
        return valores['valor__sum'] if valores['valor__sum'] else 0

    def calcula_percentual_gasto_por_categoria(self):
        return (self.total_gasto() * 100) / self.valor_planejamento
```

Adicione a chamada das funções no ver_planejamento.html

```python
{% for categoria in categorias %}
    <p>{{categoria}}</p>
    <div>
    <span style="float: left !important;">R$ {{categoria.total_gasto}}</span>
    <span style="float: right !important;">R$ {{categoria.valor_planejamento}}</span>
    </div>
    <div class="progress">
        <div class="progress-bar progress-bar-striped bg-info" role="progressbar" style="width: {{categoria.calcula_percentual_gasto_por_categoria}}%" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
    </div>
    <br>
{% endfor %}
```