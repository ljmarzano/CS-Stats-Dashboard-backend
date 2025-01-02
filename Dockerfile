FROM selenium/standalone-chrome:114.0

# Instalar Python y pip
RUN apt-get update && apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Establecer la carpeta de scripts locales en el PATH
ENV PATH="/home/seluser/.local/bin:$PATH"

# Crear directorio de trabajo
WORKDIR /app

# Copiar los archivos al contenedor
COPY . /app

# Instalar las dependencias del proyecto
RUN pip3 install --no-cache-dir -r requirements.txt

# Comando de inicio
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
