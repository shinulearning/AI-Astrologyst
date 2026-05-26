# AI_Astrologyst

Lightweight Vedic Astrology web app (React frontend + Flask backend).

Quick start

1. Backend (Python/Flask)

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
set FLASK_APP=app.py
flask run
```

2. Frontend (React + Vite)

```powershell
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173` for the frontend and `http://127.0.0.1:5000` for the API.

## Deployment notes

- The frontend now uses `HashRouter` to avoid 404s on refresh or direct navigation when deployed to Vercel.
- A `frontend/vercel.json` rewrite is also added so SPA routes are served from `index.html`.
- If you want clean URLs (`/report` instead of `/#/report`), keep the rewrite and switch back to `BrowserRouter`.
