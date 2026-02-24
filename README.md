# Escolinha de Futebol - Sistema Web com Flask

Aplicação web desenvolvida em Flask para gerenciamento e exibição de informações de uma escolinha de futebol.

O projeto utiliza renderização server-side com Jinja2 e estrutura modular baseada em templates reutilizáveis.

---

## Stack Tecnológica

- Python 3.x
- Flask
- Jinja2
- Bootstrap 5
- HTML5
- CSS3

---

## Arquitetura

A aplicação segue o padrão:

- `app.py` como ponto de entrada
- Separação entre lógica de aplicação e templates
- Uso de `base.html` como layout base
- Renderização dinâmica com `render_template`
- Estrutura preparada para expansão com Blueprints


---

## Conceitos Aplicados

- Template inheritance (`{% extends %}`)
- Template blocks (`{% block content %}`)
- Loop com Jinja2 (`{% for %}`)
- Sistema de Grid do Bootstrap (`col-md-*`)
- Organização de arquivos estáticos
- Separação de responsabilidades (estrutura preparada para Blueprints)

---

## Passo a Passo para execução

No terminal, digite os seguintes comandos:

 1. cd Futebol
 
 2. python -m venv venv

 3. venv\Scripts\Activate

 4. pip install -r requirements.txt

 5. python app.py
