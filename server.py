import tempfile

import cv2
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/imagen/")
async def create_upload_file(uploaded_file: UploadFile = File(...)):
    """Recibe un archivo desde una petición web para procesarlo"""

    # Se guarda la extensión original del archivo
    extension = uploaded_file.filename.split('.')[-1]

    # Se crea un archivo temporal
    file_ = tempfile.NamedTemporaryFile(suffix='.' + extension)

    # Se guarda la información recibida en un archivo temporal
    file_.write(uploaded_file.file.read())

    # Aquí se hace el procesamiento
    image = cv2.imread(file_.name)
    shape = image.shape

    # Se retorna los valores relevantes
    return {
        "width": shape[0],
        "height": shape[1],
    }