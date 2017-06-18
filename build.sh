#!/usr/bin/env bash

rm -rf ./build
mkdir -p ./build
pip install . -t ./build
mkdir -p ./dist
cd ./build
zip -r ../dist/aosbot.zip *
cd -
