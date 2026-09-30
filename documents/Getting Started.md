# Getting Started

## Prerequisites
- Python 3.11+
- Git

## 1. Clone the repository
```
git clone https://github.com/Annmaria7/insurance-policy-api.git
cd insurance-policy-api
```

## 2. Create and activate a virtual environment
```
python -m venv venv
venv\Scripts\activate        # Windows
```

## 3. Install dependencies
```
pip install -r requirements.txt
```

## 4. Run the application
```
python app.py
```

## 5. Access the API
```
http://127.0.0.1:5000
```

## Environment & Configuration
- No environment variables are required to run this locally.
- Data is stored **in memory** — restarting the app clears all policies. This is a known, intentional limitation of the current phase; see [roadmap.md](./roadmap.md) Phase 2.
- Debug mode is enabled by default for local development. Flask's built-in server is not production-safe — a production WSGI server (Gunicorn) is planned; see [roadmap.md](./roadmap.md) Phase 3.

## Next steps
- To test the API, see [testing.md](./testing.md)
- To understand the code structure, see [architecture.md](./architecture.md)