#!/usr/bin/env bash
set -e

# Install dependencies if missing
if ! command -v streamlit &> /dev/null; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
fi

# Run the app
echo "🚀 Starting the Simple Weather Chatbot..."
streamlit run app.py

