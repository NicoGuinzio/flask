from flask import Flask,render_template
from markupsafe import escape
from datetime import datetime
app = Flask(__name__)
app.debug = True

# filtros personaliados
@app.add_template_filter
def today(date):
    return date.strftime('%d-%m-%Y')

# esta es otra forma, primero se pone app sin arroba, luego el nombre de la funcion y luego como se la llama 
# app.add_template_filter(today, 'today')


@app.route('/')
@app.route('/index')
def index():
    name = 'Nico'
    friends = ['Nico','Euge','Sofi','Andalucia','Joaco']
    date = datetime.now()
    return render_template(
        'index.html',
        name = name,
        friends = friends,
        date = date
    )

@app.route('/hello')
@app.route('/hello/<name>')
@app.route('/hello/<name>/<int:age>')
def hello(name = None, age= None):
    if name == None and age == None:
        return '<h1> Hola Mundo! </h1>'
    elif age == None:
        return f'<h1>Hola,{name}!</h1>'
    else:
        return f'<h1>Hola,{name} el doble de tu edad es {age*2}!</h1>'

@app.route('/code/<path:code>')
def code(code):
    return f'<code>{escape(code)}</code>'

