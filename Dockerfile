FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/
COPY data/ data/
RUN mkdir results

ENV INPUT_FILE=data/roads.geojson
ENV OUTPUT_FILE=results/roads_with_lenght.geojson

CMD ["python", "src/main.py"]
