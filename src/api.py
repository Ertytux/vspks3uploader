from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "¡Hola Mundo!"}

@app.get("/async-example")
async def async_endpoint():
    # Simula operación asíncrona (ej. consulta a BD)
    await asyncio.sleep(1)
    return {"status": "Completado tras 1 segundo"}

