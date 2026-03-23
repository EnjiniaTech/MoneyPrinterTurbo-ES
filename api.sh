#!/bin/sh

export LISTEN_HOST="${LISTEN_HOST:-0.0.0.0}"
export PORT="${PORT:-8080}"

python main.py
