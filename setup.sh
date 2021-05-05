#!/bin/bash

# Install code and code-insiders via snap
sudo apt update
sudo apt install -y snapd
sudo snap install code --classic
sudo snap install code-insiders --classic

# Basic Test
cd basic
rm -rf env
python3 -m venv env

# Flask Test
cd ../flask
rm -rf env
python3 -m venv env
source ./env/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r ./requirements.txt
deactivate
