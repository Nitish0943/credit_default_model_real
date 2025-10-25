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

## Short report

### Problem

Predicting credit card payment default is important for banks and lenders to manage risk and allocate capital. The goal of this project is to provide a lightweight, user-facing tool that predicts whether a customer will default on their next payment using historical billing and payment features.

### Approach

We trained a supervised classification model on the UCI Credit Card dataset. The application loads a pre-trained model (`credit_default_model.pkl`) and exposes a Streamlit interface (`app.py`) to collect a few key features (limit balance, demographics, recent bill and payment amounts, and payment status) and produce a default probability and binary prediction.

### Results

The app returns a probability score and a binary decision (likely to default / not likely to default). Model performance on validation data achieved reasonable discrimination (see `EDA.ipynb` for metrics and visualizations). Exact metrics (AUC, precision, recall) are available in the EDA notebook and model training artifacts.

### Discussion

This Streamlit app is a demo for model consumption and quick exploration. For production use, consider the following improvements:

- Host the model artifact outside the git repository (object storage) if it is large.
- Add input validation and user authentication for the web interface.
- Implement model monitoring and periodic re-training to handle data drift.
- Expand features and perform robust cross-validation and calibration for more reliable probability estimates.

These changes make the tool safer and more reliable for real-world deployment.