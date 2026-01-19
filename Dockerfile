FROM python:3.11-slim

WORKDIR /app

# Függőségek másolása és telepítése
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kód és adatok másolása
COPY src/ src/
COPY data/ data/
COPY results/ results/

# Környezeti változók
ENV INPUT_FILE=data/roads.geojson
ENV OUTPUT_FILE=results/roads_with_length.geojson

# Program futtatása
CMD ["python", "src/main.py"]
