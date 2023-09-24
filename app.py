from flask import Flask,render_template,url_for
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


#Funcion personalizada
@app.add_template_global
def repeat(string,numero):
    return string*numero


# @app.add_template_global(repeat, 'repeat')

@app.route('/')
@app.route('/index')
def index():
    print(url_for('index'))
    print(url_for('hello', name = 'Alex', age = '27'))
    print(url_for('code', code ='print("hola")'))
    name = 'Nico'
    friends = ['Nico','Euge','Sofi','Andalucia','Joaco']
    date = datetime.now()
    return render_template(
        'index.html',
        name = name,
        friends = friends,
        date = date,
    )

@app.route('/hello')
@app.route('/hello/<name>')
@app.route('/hello/<name>/<age>')
@app.route('/hello/<name>/<int:age>/<email>')
def hello(name = None, age= None, email=None):
    my_data = {
        'name' : name,
        'age': age,
        'email' : email
    }
    
    return render_template('hello.html', data = my_data)

@app.route('/code/<path:code>')
def code(code):
    return f'<code>{escape(code)}</code>'

