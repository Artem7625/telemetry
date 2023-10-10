from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.router import router as user_router
from telemetry.router import router as telemetry_router


app = FastAPI()

app.include_router(user_router)
app.include_router(telemetry_router)

app.mount("/static", StaticFiles(directory="templates"))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8082, reload=True)
