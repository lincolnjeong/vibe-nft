from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from routers import webhooks

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.include_router(webhooks.router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/liff", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
