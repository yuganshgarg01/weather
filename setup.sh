#!/usr/bin/env bash
set -e


pip install --upgrade pip
pip install -r requirements.txt


echo "\n✅ Setup complete. To run the chatbot:"
echo "streamlit run app.py"
