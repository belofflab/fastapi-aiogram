from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.database.connection import database
from src.routers import info

app = FastAPI()
app.mount("/media", StaticFiles(directory="media"), name="media")

@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()

@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()


app.include_router(info.router)