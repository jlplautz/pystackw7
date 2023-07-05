Crie um app para o extrato

```python
python3 manage.py startapp extrato
```
Instale o app!
Crie uma URL para o extrato:
path('extrato/', include('extrato.urls')),
​
Crie uma URL para página de novo_valor:
from django.urls import path
from . import views

urlpatterns = [
    path('novo_valor/', views.novo_valor, name="novo_valor"),
]
​
Crie a view novo_valor:
def novo_valor(request):
    if request.method == "GET":
        contas = Conta.objects.all()
        categorias = Categoria.objects.all() 
        return render(request, 'novo_valor.html', {'contas': contas, 'categorias': categorias})
​
Crie o html novo_valor:
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
        <span class="fonte-destaque">Adicionar entradas/saídas</span>
        <div class="row">

            <div class="col-md-7">
                <form action="" method="POST">{% csrf_token %}
                    <div class="row">
                        <div class="col-md">
                            <label>Valor</label>
                            <input name="valor" type="text" class="form-control">
                        </div>

                        <div class="col-md">
                            <label>Categoria</label>
                            <select name="categoria" class="form-select">
                                <option value="1">Lazer</option>
                               
                            </select>
                        </div>
                    </div>
                    <br>
                    <label>Descrição</label>
                    <textarea name="descricao" class="form-control"></textarea>
                    <br>
                    <div class="row">
                        <div class="col-md">
                            <label>Data</label>  
                            <input name="data" type="date" class="form-control">
                        </div>

                        <div class="col-md">
                            <label>Conta</label>
                            <select name="conta" class="form-select">
                                <option value="1">Nubank</option>
                            </select>
                        </div>
                    </div>
                    <br>
                    <input type="radio" name="tipo" value="E"> <label class="positivo">Entrada</label>
                    <input type="radio" name="tipo" value="S"> <label class="negativo">Saída</label>
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
​
Crie as models Valores:
class Valores(models.Model):
    choice_tipo = (
        ('E', 'Entrada'),
        ('S', 'Saída')
    )
    
    valor = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    descricao = models.TextField()
    data = models.DateField()
    conta = models.ForeignKey(Conta, on_delete=models.DO_NOTHING)
    tipo = models.CharField(max_length=1, choices=choice_tipo)

    def __str__(self):
        return self.descricao
​
Execute as migrações
Envie os dados do FORM para novo_valor:
<form action="{% url 'novo_valor' %}" method="POST">{% csrf_token %}
​
Exiba as categorias dinamicamentes:
<select name="categoria" class="form-select">
    {% for categoria in categorias %}
        <option value="{{categoria.id}}">{{categoria}}</option>
    {% endfor %}
</select>
​
Exiba as contas dinamicamente:
<select name="conta" class="form-select">
    {% for conta in contas %}
        <option value="{{conta.id}}">{{conta}}</option>
    {% endfor %}
</select>
​
Crie a view novo_valor para salvar os dados:
def novo_valor(request):
    if request.method == "GET":
        contas = Conta.objects.all()
        categorias = Categoria.objects.all() 
        return render(request, 'novo_valor.html', {'contas': contas, 'categorias': categorias})
    elif request.method == "POST":
        valor = request.POST.get('valor')
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data')
        conta = request.POST.get('conta')
        tipo = request.POST.get('tipo')
        
        valores = Valores(
            valor=valor,
            categoria_id=categoria,
            descricao=descricao,
            data=data,
            conta_id=conta,
            tipo=tipo,
        )

        valores.save()

        conta = Conta.objects.get(id=conta)

        if tipo == 'E':
            conta.valor += int(valor)
        else:
            conta.valor -= int(valor)

        conta.save()

        

        messages.add_message(request, constants.SUCCESS, 'Categoria cadastrada com sucesso')
        return redirect('/extrato/novo_valor')
​
