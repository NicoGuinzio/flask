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

Puedes utilizar filtros propios de Flask en tus plantillas HTML agregándolos después de la variable, separados por `|`.

También puedes crear tus propios filtros siguiendo el formato de funciones de Python y utilizando `@app.add_template_filter()` en la línea superior de la función.
