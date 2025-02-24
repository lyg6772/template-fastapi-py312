#!/bin/bash

# 설정할 Python 버전
TARGET_PYTHON_VERSION="3.12"

if ! command -v poetry &>/dev/null; then
    echo "Poetry is not installed. Please install Poetry first."
    exit 1
fi


if ! python$TARGET_PYTHON_VERSION --version &>/dev/null; then
    echo "Python $TARGET_PYTHON_VERSION is not installed. Please install it first."
    exit 1
fi

poetry config virtualenvs.in-project true

poetry install --dev

echo "Environment setup is complete. The virtual environment is located in the .venv folder."
