# Curso de Flask con Python

## Configuración del Entorno Virtual

Para crear un entorno virtual, ejecuta el siguiente comando:

py -m venv nombre_del_entorno

Para activar el entorno virtual, utiliza:

Scripts\activate

Para desactivar el entorno virtual, ejecuta:

deactivate

## Modo de Depuración

Puedes activar el modo DEBUG en Flask utilizando el siguiente comando:

flask --app nombre_de_la_aplicacion --debug run

Para ejecutar la aplicación creada, utiliza:

flask --app nombre_de_la_aplicacion run

**Nota:** No renombres el archivo como "flask", ya que podría causar problemas.

## Renderización de HTML

Para renderizar HTML en Flask, sigue estos pasos:

1. Crea una carpeta llamada "templates".
2. Importa `render_template` de Flask.
3. Dentro de la función que retorna el HTML, utiliza `render_template('ruta_del_archivo.html')`.

## Bloques de Contenido

Para crear bloques de contenido en tus plantillas HTML, utiliza la siguiente sintaxis:

{% block nombre_del_contenido %}
{% endblock %}

## Filtros y Funciones

--> Puedes utilizar filtros propios de Flask en tus plantillas HTML agregándolos después de la variable, separados por `|`.

--> También puedes crear tus propios filtros siguiendo el formato de funciones de Python y utilizando "@app.add_template_filter()" en la línea superior de la función.

# Funciones personalizadas
Las misma se crean en el code de la app python:
--> LLamado 1: se las llama dentro de la ruta en donde se quiera agregar y luego se la inserta en el html entre {{}} (llaves dobles) 

--> LLmado 2: se lo agrega en una funcion decoradora global "@app.add_template_global" o @app.add_template_global(repeat, 'repeat')


## Envio de datos
Para el envio de datos, lo que se hace es trabajar un un diccionario de python para luego poder llamarlo por su nombre dentro del html y la logia se ubica tambien dentro del html
Codigo python>>
    @app.route('/hello/<name>/<int:age>/<email>')
    def hello(name = None, age= None, email=None):
        my_data = {
            'name' : name,
            'age': age,
            'email' : email
        }
Codigo html>>
        h2  Mis datos/h2 
        ul 
            li Nombre: {{data.name}}/li 
            li Edad: {{data.age}}/li    
            li Email: {{data.email}}/li 
        /ul 

## Enlaces y reutas
Para navegar entre las paginas, se fabrican rutas, para crear estas se usa la funcion url_for que se debe importar desde flask.
La funcion url_for se agrega debajo de las funciones creadas para la app. ej: index.
Luego se las llama en el html. ej: href="{{ url_for('index') }}"