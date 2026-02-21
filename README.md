# CoLabAI-2.0

A small Flask app that provides simple project/task management APIs and a front-end in `templates/index.html`.

## Quick start

1. Create a virtual environment and activate it:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1    # PowerShell
# or .\venv\Scripts\activate    # cmd.exe
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the app:

```powershell
python app.py
```

Open http://localhost:5000 in your browser.

## Files

- `app.py` – Flask application and API routes.
- `templates/index.html` – Front-end UI.
- `static/style.css` – Stylesheet.

## Deployment

This is a Flask app (server-side). Deployment options:

- Heroku: create a `Procfile` and deploy the Flask app.
- Vercel: use a serverless adapter or deploy as a Docker container.
- Render / fly.io: deploy a container or Python service.

If you want GitHub Pages (static only), we can extract the front-end and deploy it separately.

## Contributing

Contributions welcome — open an issue or a PR.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
