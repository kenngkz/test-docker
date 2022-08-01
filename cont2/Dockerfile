FROM test-base:latest

WORKDIR /code
COPY . .
RUN pip install -r requirements.txt

CMD ["uvicorn", "c2code:app", "--host", "0.0.0.0", "--port", "8002"]

# docker run --rm -p 8002:8002 c2