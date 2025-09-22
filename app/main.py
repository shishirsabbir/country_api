from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from contextlib import asynccontextmanager
from app.database.database import engine
from app.database.base import Base


# db initialization
async def initialize_DB():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@asynccontextmanager
async def lifespan_DB(app: FastAPI):
    await initialize_DB()
    yield


# defining app
app = FastAPI(lifespan=lifespan_DB)

BASE_DIR = Path(__file__).resolve().parent

# Mount the 'assets' directory to serve static files
app.mount("/assets", StaticFiles(directory=BASE_DIR / "public/assets"), name="assets")

# Configure Jinja2 templates
templates = Jinja2Templates(directory=BASE_DIR / "views")


@app.get("/")
def serve_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Add other routers here (e.g., auth, users, items)
