#!/usr/bin/env python
import logging
from fastapi import FastAPI, File, UploadFile
import shutil
import os

app = FastAPI()

UPLOAD_DIR = "/home/haproxy-backend1/received-images"

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.post("/upload/")
async def upload_files(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    try:
        with open(file_path, "wb") as file_object:
            shutil.copyfileobj(file.file, file_object)
        logger.info(f"Successfully uploaded file: {file.filename}")
        return {"filename": file.filename}
    except Exception as e:
        logger.error(f"Failed to upload file: {file.filename}. Error: {e}")
        return {"error": f"Failed to upload file: {file.filename}. Error: {e}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)