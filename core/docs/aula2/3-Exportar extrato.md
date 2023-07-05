Crie a URL para exportar_extrato:

```python
path('exportar_pdf/', views.exportar_pdf, name="exportar_pdf"),
```

crie o arquivo partial extrato.html:
```python
{% load static %}

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
```


instale a biblioteca para converter HTML para PDF:

```python
pip install weasyprint
```

Crie a view exportar_pdf:

```python
def exportar_pdf(request):
    valores = Valores.objects.filter(data__month=datetime.now().month)
    contas = Conta.objects.all()
    categorias = Categoria.objects.all()
    
    path_template = os.path.join(settings.BASE_DIR, 'templates/partials/extrato.html')
    path_output = BytesIO()

    template_render = render_to_string(path_template, {'valores': valores, 'contas': contas, 'categorias': categorias})
    HTML(string=template_render).write_pdf(path_output)

    path_output.seek(0)
    

    return FileResponse(path_output, filename="extrato.pdf")
```

Altere o botão para gerar o PDF:

```python
<a href="{% url 'exportar_pdf' %}" class="botao-secundario">Exportar extrato</a>
```