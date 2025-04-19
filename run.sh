#!/usr/bin/env sh

uvicorn concert_chatapp.api.routes:app \
        --host 0.0.0.0 \
        --port 8000 \
        --reload &

streamlit run concert_chatapp/ui/streamlit_ui.py \
    --server.address 0.0.0.0 \
    --server.port 8501
