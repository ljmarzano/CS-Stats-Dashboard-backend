# Utilizamos la imagen base preconfigurada con Chrome y ChromeDriver
FROM selenium/standalone-chrome:114.0

# Cambiar temporalmente al usuario root para instalar Python
USER root

# Instalamos Python y sus herramientas
RUN apt-get update && apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Volver al usuario por defecto para mayor seguridad
USER 1200

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos los archivos de la aplicación
COPY . /app

# Instalamos las dependencias de Python
RUN pip3 install --no-cache-dir -r requirements.txt

# Comando por defecto para iniciar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
