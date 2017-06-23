#!/usr/bin/env bash

set -e
source venv/bin/activate
flake8
pytest

rm -rf ./build
mkdir -p ./build
pip install . -t ./build
mkdir -p ./dist
cd ./build
zip -r ../dist/aosbot.zip *
cd -
