# backend/config.py
import os

class Config:
    # ── Anthropic (Claude) ────────────────────────────────────────────────────
    # Set in your shell: export ANTHROPIC_API_KEY="sk-ant-..."
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")

    # ── Groq (optional — only if you want to swap LLM provider) ──────────────
    # Set in your shell: export GROQ_API_KEY="gsk_..."
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")

    # ── NewsAPI ───────────────────────────────────────────────────────────────
    NEWS_API_KEY: str = os.getenv("NEWS_API_KEY", "df589199d35745ba87b9f65ad20b0442")

    # ── ChromaDB ──────────────────────────────────────────────────────────────
    # Path where ChromaDB persists its data — relative to backend/
    CHROMA_DIR: str = os.getenv("CHROMA_DIR", "./chroma_db")

    # ── Dataset paths ─────────────────────────────────────────────────────────
    DATA_DIR: str = os.getenv("DATA_DIR", "../data")
    DATASET_PATH: str = os.path.join(DATA_DIR, "startups_new_2.csv")
    LABELED_DATASET_PATH: str = os.path.join(DATA_DIR, "startups_labeled_percentile.csv")

    # ── ML Model paths ────────────────────────────────────────────────────────
    MODELS_DIR: str = "models/saved_models"
    CLASSIFIER_PATH: str  = os.path.join(MODELS_DIR, "startup_classifier.pkl")
    PREDICTOR_PATH: str   = os.path.join(MODELS_DIR, "next_round_predictor.pkl")
    SCALER_PATH: str      = os.path.join(MODELS_DIR, "scaler_next_round.pkl")
    FEATURES_PATH: str    = os.path.join(MODELS_DIR, "features_next_round.pkl")

    # ── Output directory for generated files ──────────────────────────────────
    OUTPUT_DIR: str = "generated_files"

    # ── CORS allowed origins ──────────────────────────────────────────────────
    ALLOWED_ORIGINS: list = ["*"]   # tighten in production