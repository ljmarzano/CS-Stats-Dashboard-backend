#!/bin/bash

# Instalar dependencias necesarias
apt-get update
apt-get install -y wget unzip gnupg

# Agregar la clave GPG de Google Chrome
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -

# Agregar el repositorio de Google Chrome
echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list

# Actualizar e instalar Google Chrome
apt-get update
apt-get install -y google-chrome-stable

# Descargar e instalar ChromeDriver
wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
# Mover chromedriver al directorio actual o un subdirectorio
mv chromedriver ./chromedriver
chmod +x ./chromedriver