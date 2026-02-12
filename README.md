# flask-playground

A sandbox environment for testing and experimenting with Flask.

## Quickstart

Create a virtualenv and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the app:

```bash
python app.py
```

Then open:

- `http://127.0.0.1:5000/` (returns `Hello, Flask!`)
- `http://127.0.0.1:5000/healthz` (returns JSON)
