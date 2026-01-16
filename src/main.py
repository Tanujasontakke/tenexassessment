from typing import List, Literal
from uuid import UUID

from fastapi import FastAPI,Request

from lib.todo_manager import TodoManager
from lib.models import Todo, TodoWithChildren
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
manager = TodoManager()

templates = Jinja2Templates(directory="templates")

@app.get("/todo")
async def list_all_todos() -> List[Todo]:
    return manager.get_all_todos()


@app.get("/todo/{todo_uuid}")
async def get_todo(todo_uuid: UUID) -> Todo:
    return manager.try_get_todo_by_uuid(todo_uuid)


@app.post("/todo")
async def add_todo(
    title: str, description: str, parent_uuid: str = None
) -> Todo | dict:
    try:
        result = manager.add_todo(title, description, parent_uuid)
    except ValueError as e:
        return {"error": str(e)}
    return result


@app.delete("/todo/{todo_uuid}")
async def remove_todo(todo_uuid: str) -> bool:
    return manager.remove_todo(todo_uuid)

@app.get("/",response_class=HTMLResponse)
async def home(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})