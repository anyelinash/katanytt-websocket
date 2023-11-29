FROM python:3.8

WORKDIR /app


COPY requirements.txt .

# Instala las dependencias especificadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación al directorio de trabajo
COPY . .

# Expone el puerto 8080 (o el puerto que estés utilizando para tu aplicación)
EXPOSE 5555

# Comando para ejecutar la aplicación cuando el contenedor se inicie
CMD ["python", "main.py"]
