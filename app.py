from flask import Flask,render_template
from markupsafe import escape

app = Flask(__name__)
app.debug = True

@app.route('/')
@app.route('/index')
def index():
    name = None
    friends = ['Nico','Euge','Sofi','Andalucia','Joaco']
    return render_template('index.html',name = name, friends = friends)
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


if __name__ == "__main__":
    app.run()