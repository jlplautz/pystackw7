Crie o app contas:

```python
python3 manage.py startapp contas
```

Instale o app!

Crie a URL para o app contas:

```python
path('contas/', include('contas.urls'))
```

Crie a URL para definir_contas:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('definir_contas/', views.definir_contas, name="definir_contas"),
]
```

Crie a view definir_contas:

```python
def definir_contas(request):
    if request.method == "GET":
        categorias = Categoria.objects.all()
        return render(request, 'definir_contas.html', {'categorias': categorias})
```

Crie o HTML definir_contas.html:

```python
{% extends 'bases/base.html' %}
{% load static %}
{% block 'head' %}

    <link href="{% static 'perfil/css/home.css' %}" rel="stylesheet">
    <link href="{% static 'perfil/css/gerenciar.css' %}" rel="stylesheet">

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
        <span class="fonte-destaque">Adicionar contas mensais</span>
        <div class="row">

            <div class="col-md-7">
                <form action="{% url 'definir_contas' %}" method="POST">{% csrf_token %}
                    <div class="row">
                        <div class="col-md">
                            <label>Título</label>
                            <input name="titulo" type="text" class="form-control">
                        </div>

                        <div class="col-md">
                            <label>Categoria</label>
                            <select name="categoria" class="form-select">
                                {% for categoria in categorias %}
                                    <option value="{{categoria.id}}">{{categoria}}</option>
                                {% endfor %}
                            </select>
                        </div>
                    </div>
                    <br>
                    <label>Descrição</label>
                    <textarea name="descricao" class="form-control"></textarea>
                    <br>
                    <div class="row">
                        <div class="col-md">
                            <label>Valor</label>  
                            <input name="valor" type="number" class="form-control">
                        </div>

                        <div class="col-md">
                            <label>Dia de pagamento</label>
                            <input name="dia_pagamento" min="1" max="31" type="number" class="form-control">
                        </div>
                    </div>
                    <br>
                    <br>
                    <input type="submit" style="width:40%;" class="botao-principal">

                </form>
            </div>

            <div class="col-md-8">
            </div>

        </div>

    </div>

{% endblock %}
```

Crie a model ContaPagar e ContaPaga:

```python
class ContaPagar(models.Model):
    titulo = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    descricao = models.TextField()
    valor = models.FloatField()
    dia_pagamento = models.IntegerField()
    
    def __str__(self):
        return self.titulo

class ContaPaga(models.Model):
    conta = models.ForeignKey(ContaPagar, on_delete=models.DO_NOTHING)
    data_pagamento = models.DateField()
```

Execute as migrações!

Altere as views para salvar as contas:

```python
def definir_contas(request):
    if request.method == "GET":
        categorias = Categoria.objects.all()
        return render(request, 'definir_contas.html', {'categorias': categorias})
    else:
        titulo = request.POST.get('titulo')
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        valor = request.POST.get('valor')
        dia_pagamento = request.POST.get('dia_pagamento')

        conta = ContaPagar(
            titulo=titulo,
            categoria_id=categoria,
            descricao=descricao,
            valor=valor,
            dia_pagamento=dia_pagamento
        )

        conta.save()

        messages.add_message(request, constants.SUCCESS, 'Conta cadastrada com sucesso')
        return redirect('/contas/definir_contas')
```

Adicione a URL:

```python
path('ver_contas/', views.ver_contas, name="ver_contas"),
```

Crie a view ver_contas:

```python
def ver_contas(request):
    MES_ATUAL = datetime.now().month
    DIA_ATUAL = datetime.now().day
    
    contas = ContaPagar.objects.all()

    contas_pagas = ContaPaga.objects.filter(data_pagamento__month=MES_ATUAL).values('conta')

    contas_vencidas = contas.filter(dia_pagamento__lt=DIA_ATUAL).exclude(id__in=contas_pagas)
    
    contas_proximas_vencimento = contas.filter(dia_pagamento__lte = DIA_ATUAL + 5).filter(dia_pagamento__gte=DIA_ATUAL).exclude(id__in=contas_pagas)
    
    restantes = contas.exclude(id__in=contas_vencidas).exclude(id__in=contas_pagas).exclude(id__in=contas_proximas_vencimento)

    return render(request, 'ver_contas.html', {'contas_vencidas': contas_vencidas, 'contas_proximas_vencimento': contas_proximas_vencimento, 'restantes': restantes})
```

Crie o HTML:

```python
{% extends 'bases/base.html' %}
{% load static %}
{% block 'head' %}

    <link href="{% static 'perfil/css/home.css' %}" rel="stylesheet">
    <link href="{% static 'perfil/css/gerenciar.css' %}" rel="stylesheet">
    <style>
        .linha-conta{

            background-color: var(--dark-color);
            padding: 20px;
            border-radius: 10px;

        }
    </style>
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

            <div class="col-md-8">
                <p class="fonte-destaque" style="color: red;">Contas vencidas</p>
                <div class="card">
                        
                            <div class="linha-conta">
                                <div class="row">
                                    <div class="col-md text-center">
                                        Lux
                                    </div>
                                    <div class="col-md text-center">
                                        Dia:1
                                    </div>
                                    <div class="col-md text-center">
                                        <a href="#" class="botao-principal">PAGAR</a>
                                    </div> 
                                </div>
                            </div>
                       
                </div>
                <br>
                <br>
                <p class="fonte-destaque" style="color: #E96363;">Contas próximas do vencimento</p>
                <div class="card">
                    
                        
                            <div class="linha-conta">
                                <div class="row">
                                    <div class="col-md text-center">
                                        Luz
                                    </div>
                                    <div class="col-md text-center">
                                        Dia: 1
                                    </div>
                                    <div class="col-md text-center">
                                        <a href="#" class="botao-principal">PAGAR</a>
                                    </div> 
                                </div>
                            </div>
                        
                        
                    
                </div>
                <br>
                <br>
                <p class="fonte-destaque">Restantes</p>
                <div class="card">
                
                          
                            <div class="linha-conta">
                                <div class="row">
                                    <div class="col-md text-center">
                                        Luz
                                    </div>
                                    <div class="col-md text-center">
                                        Dia: 1
                                    </div>
                                    <div class="col-md text-center">
                                        <a href="#" class="botao-principal">PAGAR</a>
                                    </div> 
                                </div>
                            </div>
                        
                       
                    
                </div>

            </div>

            <div class="col-md-4">
            </div>

        </div>

    </div>

{% endblock %}
```

Exiba dinamicamente:

```python
{% for conta in contas_vencidas %}
    <div class="linha-conta">
        <div class="row">
            <div class="col-md text-center">
                {{conta}}
            </div>
            <div class="col-md text-center">
                Dia: {{conta.dia_pagamento}}
            </div>
            <div class="col-md text-center">
                <a href="#" class="botao-principal">PAGAR</a>
            </div> 
        </div>
    </div>
{% endfor %}
```

Todas as contas!

Adicione um IF para validar se existe alguma:

```python
{% if not contas_vencidas %}
    <p class="fonte-destaque">Ufa, nenhuma conta vencida.</p>

{% else %}
    {% for conta in contas_vencidas %}
        <div class="linha-conta">
            <div class="row">
                <div class="col-md text-center">
                    {{conta}}
                </div>
                <div class="col-md text-center">
                    Dia: {{conta.dia_pagamento}}
                </div>
                <div class="col-md text-center">
                    <a href="#" class="botao-principal">PAGAR</a>
                </div> 
            </div>
        </div>
    {% endfor %}
{% endif %}
```