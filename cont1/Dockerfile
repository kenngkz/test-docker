FROM test-base:latest

WORKDIR /code
COPY . .
RUN pip install -r requirements.txt

CMD ["uvicorn", "c1code:app", "--host", "0.0.0.0", "--port", "8001"]

# docker run --rm -p 8001:8001 c1