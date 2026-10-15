import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import health
from app.core.config import get_settings
from app.core.errors import register_error_handlers

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
settings = get_settings()
settings.upload_path.mkdir(parents=True, exist_ok=True)
settings.chroma_path.mkdir(parents=True, exist_ok=True)

app = FastAPI(title="AI Study Companion")
app.add_middleware(CORSMiddleware, allow_origins=[settings.frontend_origin],
                   allow_methods=["*"], allow_headers=["*"])
register_error_handlers(app)
app.include_router(health.router, prefix="/api/v1")
