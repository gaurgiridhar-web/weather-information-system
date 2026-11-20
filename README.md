# Weather Information System

A beginner-friendly Python web application that displays current weather conditions for a city.

## Technologies
- Python
- Streamlit
- Requests
- OpenWeatherMap Current Weather API
- Microsoft Azure App Service (Linux)

## Run locally (Windows PowerShell)

1. Install Python 3.11 or 3.12 and VS Code.
2. Open this folder in VS Code.
3. Open Terminal > New Terminal.
4. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

5. Install packages:

   ```powershell
   python -m pip install -r requirements.txt
   ```

6. Set your OpenWeatherMap API key for this terminal session:

   ```powershell
   $env:OPENWEATHER_API_KEY="YOUR_REAL_API_KEY"
   ```

7. Run the app:

   ```powershell
   python -m streamlit run app.py
   ```

8. Open the local address printed in the terminal (normally http://localhost:8501).

## Deploy to Azure App Service (Portal + GitHub)

1. Push the project files to a GitHub repository. Do not upload your real API key.
2. In https://portal.azure.com, create an App Service Web App:
   - Publish: Code
   - Operating System: Linux
   - Runtime: Python 3.12 (or a Python version offered by your region)
   - Select a pricing plan only after checking its cost.
3. In the Web App, open Deployment Center and connect the GitHub repository and `main` branch. Choose GitHub Actions if prompted.
4. In Settings > Environment variables, add:
   - Name: `OPENWEATHER_API_KEY`
   - Value: your real OpenWeatherMap API key
   Save the setting.
5. In Settings > Configuration > General settings, set Startup Command to:

   ```bash
   python -m streamlit run app.py --server.port 8000 --server.address 0.0.0.0 --server.headless true
   ```

6. Ensure build automation is enabled. If needed, add this app setting:
   - `SCM_DO_BUILD_DURING_DEPLOYMENT` = `true`
7. Save settings, restart the Web App, and check Deployment Center > Logs.
8. Open the Default Domain from the Web App Overview page.

## Notes
- This project displays current weather conditions, not a multi-day forecast.
- OpenWeatherMap API keys may take time to activate.
- Keep the API key private. Never commit it to GitHub.
- Azure pricing and free-tier availability depend on your subscription and region.
