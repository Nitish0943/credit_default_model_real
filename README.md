# credit_default_model_real

## Deploying to Render

This repository contains a Streamlit app (`app.py`) that predicts credit card default using a pre-trained model file `credit_default_model.pkl`.

Quick steps to deploy on Render:

1. Push this repository to a Git provider (GitHub, GitLab, Bitbucket).
2. Create a new Web Service on Render and connect the repository.
3. Render will detect Python. Set the build command (if prompted) to:

	pip install -r requirements.txt

4. Set the start command to:

	streamlit run app.py --server.port $PORT --server.enableCORS false

5. Ensure the model file `credit_default_model.pkl` is present in the repository (it is included in this repo).

Notes:
- This repo includes a `Procfile` and `render.yaml` with a recommended start command. You can either use those or provide the start command directly in the Render dashboard.
- If you need a specific Python runtime, add a `runtime.txt` with e.g. `python-3.11.4` (optional). Render will use a supported Python version if not specified.

Troubleshooting:
- If the app fails to start, check the Render build logs for missing packages and ensure `requirements.txt` lists them. Add any extra packages as needed.
- If Streamlit complains about CORS or port, the `--server.enableCORS false` and `$PORT` in the start command should resolve common issues.

Enjoy! 🚀