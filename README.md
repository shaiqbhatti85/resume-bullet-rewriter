# Resume Bullet Rewriter ✦

An AI-powered Streamlit app that rewrites weak resume bullets into 3 strong variants using Claude.

## Setup

```bash
# 1. Clone / navigate to the project folder
cd resume-rewriter

# 2. Create a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate      # macOS / Linux
.venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run main.py
```

## Usage

1. Open the app in your browser (usually http://localhost:8501)
2. Enter your **Anthropic API key** in the expander at the bottom of the controls
3. Pick a **Role** and **Tone / Focus**
4. Paste your weak bullet point
5. Click **Rewrite Bullet**
6. Copy any of the 3 generated variants

## Project Structure

```
resume-rewriter/
├── main.py          # Streamlit UI and app logic
├── rewriter.py      # Anthropic API calls and prompt engineering
├── styles.py        # Custom CSS injected into Streamlit
├── requirements.txt
└── README.md
```

## Getting an API Key

Get your key from https://console.anthropic.com — the key starts with `sk-ant-`.
