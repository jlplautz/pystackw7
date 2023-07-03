## Perfil

Crie uma URL para a HOME:

Crie a view home:

```python
def home(request):
    return render(request, 'home.html')
```

Configure onde o Django irá procurar por HTML:

```python
os.path.join(BASE_DIR, 'templates')
```

Crie o arquivo base.html em templates/bases:

```jsx
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>{% block 'title' %}{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    {% block 'head' %}{% endblock %}
  
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-dark" style="background-color: #201F1F;">
        <a class="navbar-brand" style="margin-left: 30px" href="">FINAN.CE</a>
    </nav>
    {% block 'body' %}{% endblock %}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>
```

Crie o home.html

```jsx
{% extends 'bases/base.html' %}

{% block 'body' %}
    <div class="container">
        <br>
        <br>
        <div class="row">
            <div class="col-md-3">
                <a style="text-decoration: none; color:white;" href="#">
                    <div class="card">
                        <div class="row">
                            <div class="col-md-8">
                                <span  class="fonte-destaque">RS 1.000,00</span>
                            </div>
                            <div class="col-md">
                                <img class="icone-setas" src="#">
                            </div>
                        </div>
        
                    </div>
                </a>
            </div>
            <div class="col-md-3">
                <a style="text-decoration: none; color:white;" href="#">
                    <div class="card">
                        <div class="row">
                            <div class="col-md-8">
                                <span  class="fonte-destaque">RS 1.000,00</span>
                            </div>
                            <div class="col-md">
                                <img class="icone-setas" src="#">
                            </div>
                        </div> 
                    </div>
                </a>
            </div>
        </div>
        <br>
        <br>
       
        <div class="row">

            <div class="col-md-4">
                <div class="card">
                    <div class="saldo">
                        <span class="fonte-destaque">Saldo total</span>
                        <br>
                        <span class="font-light">R$ 1.200,00</span>
                    </div>
                    <hr class="hr-borda">
                    <span class="fonte-destaque">Suas contas</span>

                    <div class="div-contas">
                        
                            <div class="lista-conta">
                                <span>Nubank</span>
                                <span class="total-conta">R$ 3.000,00</span>
                            </div>
                            <br>
                        
                        
                        
                    </div>
                    <hr class="hr-borda">
                    <a href="#" class="botao-principal">Gerenciar contas</a>
                </div>
                
            </div>

            <div class="col-md-8">
                <div class="card">
                    <div class="row">
                        <div class="col-md">
                            <div class="saldo">
                                <span class="fonte-destaque">Saldo mensal</span>
                                <br>
                                <span class="font-light">R$ 0.000,00</span>
                            </div>
                        </div>
                        <div class="col-md">
                            <div class="despesa">
                                <span class="fonte-destaque">Despesa mensal</span>
                                <br>
                                <span class="font-light">R$ 0.000,00</span>
                            </div>

                        </div>

                    </div>
                    <hr class="hr-borda">
                    <span class="fonte-destaque">Total livre</span>
                    <span class="font-light negativo">R$ 0.000,00</span>
                    <hr class="hr-borda">
                    <a href="#" class="botao-principal">Gerenciar dados mensais</a>
                </div>
            </div>

        </div>
        <br>
        <div class="row">
            <div class="col-md-4">
                <div class="card">
                    <div class="saldo">
                        <span class="fonte-destaque">Planejamento</span>
                    </div>
                    <hr class="hr-borda">
                    <a href="#" class="botao-principal">Definir planejamento</a>
                </div>
            </div>
            <div class="col-md-8">
                <div class="card">
                    <span class="fonte-destaque">Equilibrio financeiro</span>
                    <hr class="hr-borda">

                    <p>Gastos essenciais</p>
                    <div class="progress">
                        <div class="progress-bar progress-bar-striped bg-info" role="progressbar" style="width: 20%" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                    <br>
                    <p>Gastos não essenciais</p>
                    <div class="progress">
                        <div class="progress-bar progress-bar-striped bg-info" role="progressbar" style="width: 40%" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
                    </div>

                    <hr class="hr-borda">
                    <a href="#" class="botao-principal">Alterar categorias essenciais</a>

                </div>
            </div>
        </div>
        <br>
        <div class="row">
            <div class="col-md-4">
            </div>
            
            <div class="col-md-8">
                <div class="card">
                    <span class="fonte-destaque">Gerenciar contas</span>
                    <hr class="hr-borda">

                    <span class="fonte-destaque">Próximas do vencimento</span>
                    <span class="fonte-light">3 contas próximas do vencimento</span>
                    <br>
                    <span class="fonte-destaque negativo">Vencidas</span>
                    <span class="fonte-light">0 contas vencidas</span>

                    <hr class="hr-borda">
                    
                    <a href="#" class="botao-principal">Ver mais</a>

                </div>
            </div>
        </div>
        <br>
        <br>
    </div>
{% endblock %}
```

Configure os arquivos estáticos:

```jsx
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'templates/static'),)
STATIC_ROOT = os.path.join('static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

Crie o base.css em templates/static/geral/css

```jsx
body{
    background-color: #1C1A1A !important;
    color: white !important;
}

:root{
     
    --main-color: #2B2B2B;
    --dark-color: #1C1A1A;
    --contrast-color: #69D2CD;
    --differential-color: #E96363;

}
```

Importe o base.css em base.html

```jsx
<link href="{% static 'geral/css/base.css' %}" rel="stylesheet">
```

Crie o home.css

```jsx
.card{

    width: 100%;
    background-color: var(--main-color);
    padding: 20px;

}

.saldo{
    border-left: 2px solid var(--contrast-color);
    padding-left: 10px;
}

.fonte-destaque{

    font-weight: bold;
    font-size: 25px;

}

.font-light{

    font-weight: 200;

}

.hr-borda{
    color: var(--dark-color);
}

.lista-conta{
    background-color: var(--dark-color);
    padding: 8px;
    border-radius: 10px;

}
.total-conta{
    color: #B9F1D6;
    font-weight: 200;
    float: right;
}

.botao-principal{

    text-decoration: none;
    color: black;
    font-weight: bold;
    font-size: 18px;

    padding: 10px;
    background-color: var(--contrast-color);
    text-align: center;
    border-radius: 15px;
    border: none;

}

.despesa{
    border-right: 2px solid var(--differential-color);
    text-align: right;
    padding-right: 10px;
}

.negativo{
    color: var(--differential-color);
}

.positivo{
    color: var(--contrast-color);
}

.icone-setas{
    width: 50%;
    display: inline;
}
```

Adicione as imagens:

![entradas.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2fbac0a6-216e-4501-905f-9c0f48d27697/entradas.png)

![saidas.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/dc7615f5-71ff-4e41-8b79-6a8385d8bf92/saidas.png)

![exit.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3128d42c-627d-4f67-b76f-b7c16417181f/exit.png)

![check.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8ef32d61-7cf2-44bf-b049-61c4825406a0/check.png)

```jsx
<img class="icone-setas" src="{% static 'perfil/img/entradas.png' %}">

<img class="icone-setas" src="{% static 'perfil/img/saidas.png' %}">
```

Agora crie a URL para gerenciar:

```python
path('gerenciar/', views.gerenciar, name="gerenciar"),
```

Crie a VIEW gerenciar:

```python
def gerenciar(request):
    return render(request, 'gerenciar.html')
```

Crie o gerenciar.html

```python
{% extends 'bases/base.html' %}
{% load static %}
{% block 'head' %}

    <link href="{% static 'perfil/css/home.css' %}" rel="stylesheet">
    <link href="{% static 'perfil/css/gerenciar.css' %}" rel="stylesheet">

{% endblock %}

{% block 'body' %}
    <br>
    <br>
    <div class="container">
        <div class="row">
            <div class="col-md-5">
                <p class="fonte-destaque">Suas contas</p>
                <hr>

                <div class="contas">

                    
                        <div class="lista-contas-main">
                            <span><img width="10%" src="#">&nbsp&nbspNubank</span>

                            <span class="total-conta positivo ">R$ 1.800,00&nbsp&nbsp&nbsp <a href="#"><img src="{% static 'perfil/img/exit.png' %}"></a></span>
                        </div>
                        <br>
                    
                    
                </div>

                <hr>
                <span class="fonte-destaque">Total:</span>
                <span class="positivo total-conta font-destaque">R$ 1.800,00</span>
            </div>

            <div class="col-md-2"></div>

            <div class="col-md-5">
                <p class="fonte-destaque">Nova conta</p>
                
                <form action="" method="POST">
                    <label>Apelido</label>
                    <input type="text" name="apelido" class="form-control" placeholder="">
                    <br>
                    <label>Banco</label>
                    <select name="banco" class="form-select">
                        <option value="NU">Nubank</option>
                    </select>
                    <br>
                    <label>Tipo</label>
                    <select name="tipo" class="form-select">
                        <option value="pf">Pessoa física</option>
                        <option value="pj">Pessoa jurídica</option>
                    </select>
                    <br>
                    <label>Valor</label>
                    <input type="number" name="valor" class="form-control" placeholder="">
                    <br>
                    <input type="file" placeholder="Ícone" name="icone">
                    <br>
                    <br>
                    <input style="width: 100%" type="submit" class="botao-principal">
                </form>
            </div>
        </div>

        <hr>

        <div class="row">
            <div class="col-md-5">
                <span class="fonte-destaque">Nova categoria</span>

                <form action="" method="POST">
                    <label>Categoria</label>
                    <input type="text" name="categoria" class="form-control">
                    <br>

                    <input type="checkbox" name="essencial" value="essencial"><label class="positivo">&nbspEssencial</label>
                    <br>
                    <br>
                    <input style="width: 100%" type="submit" class="botao-principal" value="Adicionar">
                </form>
            </div>

            <div class="col-md-2">
            </div>

            <div class="col-md-5">
                <span class="fonte-destaque">Suas categoria</span>
                <br>
                <div class="contas">

                    
                        <div class="lista-contas-main">
                            <span>Lazer</span>

                            <span class="total-conta"><a href="#"><img src="#"></a></span>
                        </div>
                        <br>
                   
                    
                </div>
            </div>
        </div>
    </div>
{% endblock %}
```

Crie as models Categoria e Conta:

```python
from django.db import models

# Create your models here.

class Categoria(models.Model):
    categoria = models.CharField(max_length=50)
    essencial = models.BooleanField(default=False)
    valor_planejamento = models.FloatField(default=0)

    def __str__(self):
        return self.categoria

class Conta(models.Model):
    banco_choices = (
        ('NU', 'Nubank'),
        ('CE', 'Caixa econômica'),
    )

    tipo_choices = (
        ('pf', 'Pessoa física'),
        ('pj', 'Pessoa jurídica'),
    )

    apelido = models.CharField(max_length=50)
    banco = models.CharField(max_length=2, choices=banco_choices)
    tipo = models.CharField(max_length=2, choices=tipo_choices)
    valor = models.FloatField()
    icone = models.ImageField(upload_to='icones')

    def __str__(self):
        return self.apelido
```

Execute as migrações!

Altere o FORM de cadastrar uma nova conta para enviar os dados:

```python
<form action="{% url 'cadastrar_banco' %}" method="POST" enctype='multipart/form-data'>{% csrf_token %}
```

Crie a url cadastrar_banco:

```python
path('cadastrar_banco/', views.cadastrar_banco, name="cadastrar_banco"),
```

Crie a view cadastrar_banco

```python
def cadastrar_banco(request):
    apelido = request.POST.get('apelido')
    banco = request.POST.get('banco')
    tipo = request.POST.get('tipo')
    valor = request.POST.get('valor')
    icone = request.FILES.get('icone')
    
    if len(apelido.strip()) == 0 or len(valor.strip()) == 0:
        return redirect('/perfil/gerenciar/')
    
    conta = Conta(
        apelido = apelido,
        banco=banco,
        tipo=tipo,
        valor=valor,
        icone=icone
    )

    conta.save()

    return redirect('/perfil/gerenciar/')
```

Configure as mensagens:

```python
from django.contrib.messages import constants

MESSAGE_TAGS = {
    constants.DEBUG: 'alert-primary',
    constants.ERROR: 'alert-danger',
    constants.WARNING: 'alert-warning',
    constants.SUCCESS: 'alert-success',
    constants.INFO: 'alert-info ',
}
```

Crie a mensagem:

```python
messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
```

Exiba a mensagem no HTML:

```python
{% if messages %}
    {% for message in messages %}
        <div class="alert {{ message.tags }}">{{ message }}</div>
    {% endfor %}
{% endif %}
```

Busque todas as contas cadastradas e envie para o HTML:

```python
def gerenciar(request):
    contas = Conta.objects.all()
    return render(request, 'gerenciar.html', {'contas': contas,})
```

Adicione uma URL para os arquivos de media:

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('perfil/', include('perfil.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

Agora liste as contas:

```python
{% for conta in contas %}
    <div class="lista-contas-main">
        <span><img width="10%" src="{{conta.icone.url}}">&nbsp&nbsp{{conta}}</span>

        <span class="total-conta positivo ">R$ {{conta.valor}}</span>
    </div>
    <br>
{% endfor %}
```

Calcule o total de todas as contas na view e exiba no HTML:

```python
def gerenciar(request):
    contas = Conta.objects.all()
    #total_contas = contas.aggregate(Sum('valor'))
    total_contas = 0

    for conta in contas:
        total_contas += conta.valor
    return render(request, 'gerenciar.html', {'contas': contas, 'total_contas': total_contas})
```

Crie um link para deletar uma conta:

```python
<a href="/perfil/deletar_banco/{{conta.id}}"><img src="{% static 'perfil/img/exit.png' %}"></a>
```

Crie a URL deletar_banco:

```python
path('deletar_banco/<int:id>', views.deletar_banco, name="deletar_banco"),
```

Crie a view deletar_banco:

```python
def deletar_banco(request, id):
    conta = Conta.objects.get(id=id)
    conta.delete()
    
    messages.add_message(request, constants.SUCCESS, 'Conta removida com sucesso')
    return redirect('/perfil/gerenciar/')
```

Atualize o FORM de categoria:

```python
<form action="{% url 'cadastrar_categoria' %}" method="POST">{% csrf_token %}
```

Crie a URL cadastrar_categoria:

```python
path('cadastrar_categoria/', views.cadastrar_categoria, name="cadastrar_categoria"),
```

Crie a VIEW cadastrar_categoria:

```python
def cadastrar_categoria(request):
    nome = request.POST.get('categoria')
    essencial = bool(request.POST.get('essencial'))

    categoria = Categoria(
        categoria=nome,
        essencial=essencial
    )

    categoria.save()

    messages.add_message(request, constants.SUCCESS, 'Categoria cadastrada com sucesso')
		return redirect('/perfil/gerenciar/')
```

Em gerenciar busque todas as categorias:

```python
def gerenciar(request):
    contas = Conta.objects.all()
    categorias = Categoria.objects.all()
    #total_contas = contas.aggregate(Sum('valor'))
    total_contas = 0

    for conta in contas:
        total_contas += conta.valor

    print(total_contas)
    return render(request, 'gerenciar.html', {'contas': contas, 'total_contas': total_contas, 'categorias': categorias})
```

Crie a URL update_categoria:

```python
path('update_categoria/<int:id>', views.update_categoria, name="update_categoria"),
```

Crie a view update_categoria:

```python
def update_categoria(request, id):
    categoria = Categoria.objects.get(id=id)

    categoria.essencial = not categoria.essencial

    categoria.save()

    return redirect('/perfil/gerenciar/')
```

Adicione o link de redirecionamento:

```python
<a href="{% url 'update_categoria' categoria.id %}"><img src="{% if categoria.essencial %}{% static 'perfil/img/check.png' %}{% else %}{% static 'perfil/img/exit.png' %}{% endif %}"></a>
```

Em utils crie a função calcula_total:

```python
def calcula_total(obj, campo):
    total = 0
    for i in obj:
        total += getattr(i, campo)

    return total
```

Altere a view home para:

```python
def home(request):
    contas = Conta.objects.all()
    saldo_total = calcula_total(contas, 'valor')
    return render(request, 'home.html', {'contas': contas, 'saldo_total': saldo_total,})
```