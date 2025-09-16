## Deep Search - Setup Guide

### Requirements
- uv (Python package manager). Follow the instructions here to install uv https://docs.astral.sh/uv/getting-started/installation/
- openai api key
- google gemini api 
- google programable search (api key & search engine id)
- sendgrid api key

### 1) Create and sync a venv with uv
```bash
cd /Users/youruser/projects
git clone https://github.com/noimo-analytics/deep_research.git
cd deep_research
uv sync
```

If you plan to use agent graph visualization:
```b
# macOS system dependency
port install graphviz
uv pip install "openai-agents[viz]" graphviz
```

### 2) Environment variables (.env)
Create a `.env` file in the project root (same folder as `pyproject.toml`). Example:
```env
# OpenAI
OPENAI_API_KEY=sk-...

# Google Gemini (OpenAI-compatible endpoint)
# Required if you use the Gemini models via the OpenAI-compatible API in the notebooks
GOOGLE_API_KEY=your_gemini_api_key

# Google Programmable Search (Custom Search API)
# API key from Google Cloud; enable "Custom Search API" for this key
GOOGLE_CUSTOM_SEARCH_API_KEY=your_google_cloud_api_key
# Search engine ID from Programmable Search Engine (Setup → Search engine ID)
# New IDs may NOT contain a colon; use exactly what Google shows.
GOOGLE_SEARCH_CONTEXT=your_search_engine_id

# SendGrid (email sending)
SENDGRID_API_KEY=your_sendgrid_api_key
# Optional if you parameterize these in code; otherwise edit app_folder/email_agent.py
FROM_EMAIL=verified_sender@example.com
TO_EMAIL=recipient@example.com

# Gradio (optional, if you add a UI)
GRADIO_SERVER_NAME=0.0.0.0
GRADIO_SERVER_PORT=7860
# Optional basic auth: "user:pass"
GRADIO_AUTH=
```

Notes:
- Programmable Search “Search engine ID” is the value used as `cx`. Recent IDs may not include a colon; use the exact value.
- Ensure your Google Cloud API key has the Custom Search API enabled and its restrictions allow calls to `customsearch.googleapis.com`.
- In `app_folder/email_agent.py`, update the hardcoded `from_email` and `to_email` or read them from `FROM_EMAIL` and `TO_EMAIL`.

### 3) Selecting the notebook kernel
- In Jupyter/VS Code, select the interpreter for the kernel as the project venv: `.venv`.

### 4) Running examples
- Notebooks: open `deedeep_research_gemini_gs_openai_manager.ipynb`, ensure the kernel is `.venv`, and run cells.
- Run python app  e.g.:
```bash
uv run app_folder/deep_research
```

### 5) Common issues
- Import error for `agents.extensions.visualization`: install both the Python package and the system Graphviz (see step 1), and ensure the notebook uses the `.venv` kernel.
- Google Custom Search 400 errors: verify `GOOGLE_SEARCH_CONTEXT` is the exact “Search engine ID”; ensure API is enabled and key restrictions are compatible.
- SendGrid: sender must be verified in your SendGrid account before emails can be sent.

