from typing import Annotated

from fastapi import APIRouter, Request, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from telemetry.enet import EnetHandler


templates = Jinja2Templates(directory="templates")

router = APIRouter(
    prefix="/telemetry",
    tags=["Telemetry"]
)

@router.get("/", response_class=HTMLResponse)
async def get_json_data(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.websocket("/ws")
async def get_streaming_data(websocket: WebSocket):
    await websocket.accept()

    enet_handler = EnetHandler()
    if enet_handler.connect("localhost", 5555):
        while True:
            parsed_data = enet_handler.receive_data()
            if parsed_data is not None:
                data = enet_handler.process_data(parsed_data)
                if data is not None:
                    if isinstance(data, dict):
                        await websocket.send_json(data)
                    elif isinstance(data, bytes):
                        await websocket.send_bytes(data)
