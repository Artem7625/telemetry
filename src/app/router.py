from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.database import get_service_data, set_engineer_name, db_dump

from app.models import EngineerName


templates = Jinja2Templates(directory="templates")

router = APIRouter(
    prefix="/service",
    tags=["Service"]
)

@router.get("/page", response_class=HTMLResponse)
async def get_testing_page(request: Request):
   return templates.TemplateResponse("user.html", {"request": request})


@router.get("/name")
async def get_json_data():
    service_data = get_service_data()
    return service_data


@router.post("/name")
async def set_user(data: EngineerName):
    name = data.name
    set_engineer_name(name=name)


@router.get("/dump")
async def dump():
    db_dump()
