# AI Study Companion (Phase 1 scaffold)

## Setup (Windows PowerShell)
```
docker compose up -d postgres
cd backend
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload --port 8000
```
Frontend (new terminal):
```
cd frontend
copy .env.example .env
npm install
npm run dev
```
Check: http://localhost:8000/api/v1/health and http://localhost:5173

Tests (Postgres running): `cd backend; pytest`

Alembic migrations arrive with the data models in Phase 2.
