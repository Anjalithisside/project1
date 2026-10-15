from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env", extra="ignore")

    database_url: str = "postgresql+psycopg://studyuser:studypass@localhost:5432/studycompanion"
    groq_api_key: str = ""
    groq_model: str = ""
    jina_api_key: str = ""
    jina_embedding_model: str = "jina-embeddings-v3"
    frontend_origin: str = "http://localhost:5173"
    upload_dir: str = "data/uploads"
    chroma_dir: str = "data/chroma"
    max_upload_mb: int = 25
    chunk_size: int = 1000
    chunk_overlap: int = 150
    retrieval_top_k: int = 5

    @property
    def upload_path(self) -> Path:
        return (BASE_DIR / self.upload_dir).resolve()

    @property
    def chroma_path(self) -> Path:
        return (BASE_DIR / self.chroma_dir).resolve()


@lru_cache
def get_settings() -> Settings:
    return Settings()
