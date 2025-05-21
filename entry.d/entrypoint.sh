#!/bin/bash
set -x

# Nếu chưa có model → tải bằng download_models.py
if [ ! -f /models/.downloaded ]; then
  echo "🔽 Downloading models for the first time..."
  python3 /entry.d/download_models.py
  touch /models/.downloaded
fi

# Khởi động Triton
tritonserver --model-repository=/models
