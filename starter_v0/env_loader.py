from __future__ import annotations

import os
from pathlib import Path


def load_dotenv(path: Path, *, override: bool = True) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("\"'")
        if key and (override or key not in os.environ):
            os.environ[key] = value


def load_streamlit_secrets() -> None:
    """Load Streamlit Community Cloud secrets for code that uses os.getenv."""
    try:
        import streamlit as st
        from streamlit.errors import StreamlitSecretNotFoundError
    except ImportError:
        return

    try:
        for key, value in st.secrets.items():
            if key not in os.environ and isinstance(value, (str, int, float, bool)):
                os.environ[key] = str(value)
    except StreamlitSecretNotFoundError:
        return


def load_lab_env(root: Path) -> None:
    external_path = os.getenv("DAY03_ENV_FILE")
    if external_path:
        load_dotenv(Path(external_path).expanduser())
    else:
        load_dotenv(root / ".env")
    load_streamlit_secrets()
