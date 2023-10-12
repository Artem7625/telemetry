from fastapi import APIRouter, Request, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import websockets

from telemetry.enet import EnetHandler


router = APIRouter(
    prefix="/telemetry",
    tags=["Telemetry"]
)

enet_handler = EnetHandler()
templates = Jinja2Templates(directory="templates")


# Переход на страницу для тестирования WebSocket.
@router.get("/", response_class=HTMLResponse)
async def get_json_data(request: Request):
    return templates.TemplateResponse("telemetry.html", {"request": request})


@router.websocket("/ws")
async def get_streaming_data(websocket: WebSocket):
    await websocket.accept()
    await _connect_to_websocket(websocket)


async def _connect_to_websocket(websocket: WebSocket):
    """Управляет взаимодействием с тестовым Enet-сервером."""

    if await enet_handler.connect("localhost", 5555):
        try:
            while True:
                parsed_data = await enet_handler.receive_data()
                if parsed_data is not None:
                    await _send_data(websocket, parsed_data)
        except websockets.exceptions.ConnectionClosedOK:
            pass
        finally:
            await enet_handler.disconnect()


async def _send_data(websocket: WebSocket, parsed_data):
    """Отправляет данные через web-soket, в зависимости от их типа."""

    data = await enet_handler.process_data(parsed_data)

    if data is not None:
        if isinstance(data, dict):
            await websocket.send_json(data)
        elif isinstance(data, bytes):
            await websocket.send_bytes(data)