#!/bin/sh

# If you could not download the model from the official site, you can use the mirror site.
# Just remove the comment of the following line .
# 如果你无法从官方网站下载模型，你可以使用镜像网站。
# 只需要移除下面一行的注释即可。

# export HF_ENDPOINT=https://hf-mirror.com

STREAMLIT_SERVER_PORT="${PORT:-8501}"
STREAMLIT_SERVER_ADDRESS="${LISTEN_HOST:-0.0.0.0}"

streamlit run ./webui/Main.py \
  --server.address="${STREAMLIT_SERVER_ADDRESS}" \
  --server.port="${STREAMLIT_SERVER_PORT}" \
  --server.enableCORS=True \
  --browser.gatherUsageStats=False
