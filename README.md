# image-processing-api

API para crear una interfaz HTTP para el procesamiento de imágenes

## Instalación

Este script necesita python >= 3.6 o superior, las pruebas se hicieron en python 3.8

Para instalar los requerimientos ejecute:

    pip install -r requirements.txt

## Ejecutar el servidor

Para ejecutar el servidor ejecute:

    uvicorn server:app

## Peticiones

El servidor arrancará en http://localhost:8000

Este servidor expone un único endpoint: `/imagen/`

Para probarlo puede acceder a localhost:8000/docs, donde aparecerá un formulario web para hacer las pruebas
